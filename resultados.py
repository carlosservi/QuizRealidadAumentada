import cv2
import imutils
from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
import numpy as np
import screeninfo
from threading import Thread, Event
import speech as sp


def resultados(correctas):
    resultados = []
    reiniciar = False

    cap = cv2.VideoCapture(0)

    # Obtener las dimensiones de la pantalla
    screen_info = screeninfo.get_monitors()[0]
    screen_width = screen_info.width
    screen_height = screen_info.height

    # Configuración del texto a mostrar
    font_path = "Font/RubikDistressed-Regular.ttf"
    font_size = 38
    font_color = (255, 255, 255)  # Color blanco
    thickness = 0
    font_size2 = 70

    # Cargar la fuente personalizada
    font = ImageFont.truetype(font_path, font_size)
    font2 = ImageFont.truetype(font_path, font_size2)

    # Detector de rostros
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Crear los textos de los Resultados
    cont = 0
    res = 0
    for elemento in correctas:
        if(elemento == True):
            t = "Correcto"
            res+=2
        else:
            t = "Incorrecto"
        resultados.append("Pregunta " + str(cont) + ": " + t)
        cont+=1

    texto = "Resultados: " + str(res*10) + "%"
    despedida = "Diga Reiniciar para volver a jugar o Salir para terminar"

    while True:
        #Gestionar respuesta y reinicio
        if sp.evento.is_set():
            with sp.cerrojo:
                respuesta, r = comprobar_evento(sp.texto_reconocido)
                if r == False:
                    sp.evento.clear()
                else:
                    if respuesta == "reiniciar":
                        reiniciar = True
                    break
    
        ret, frame = cap.read()
        if ret == False:
            print("Error al acceder a la webcam")
            break

        frame = imutils.resize(frame, width=1200)

        # Detección de los rostros presentes en el fotograma
        faces = faceClassif.detectMultiScale(frame, 1.3, 5)

        # Convertir el marco de OpenCV a imagen Pillow
        img_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_pil)

        for (x, y, w, h) in faces:
            # Calcular las coordenadas superiores izquierdas de los textos para que estén centrados con el rostro
                #Texto Porcentaje
                text_width, text_height = draw.textsize(texto, font=font2)
                text_x = x + (w - text_width) // 2
                text_y = y - text_height
                # Dibujar el texto en la imagen Pillow
                draw.text((text_x, text_y), texto, font=font2, fill=font_color, stroke_width=thickness)

                #Texto Respuesta 1
                resa_width, resa_height = draw.textsize(resultados[0], font=font)
                resa_x = x + (w - resa_width) // 2 
                resa_y = y + resa_height + 20
                # Dibujar el texto en la imagen Pillow
                draw.text((resa_x, resa_y), resultados[0], font=font, fill=font_color, stroke_width=thickness)

                #Texto Respuesta 2
                resb_width, resb_height = draw.textsize(resultados[1], font=font)
                resb_x = x + (w - resb_width) // 2
                resb_y = y + resb_height + 70
                # Dibujar el texto en la imagen Pillow
                draw.text((resb_x, resb_y), resultados[1], font=font, fill=font_color, stroke_width=thickness)

                #Texto Respuesta 3
                resc_width, resc_height = draw.textsize(resultados[2], font=font)
                resc_x = x + (w - resc_width) // 2
                resc_y = y + resc_height + 120
                # Dibujar el texto en la imagen Pillow
                draw.text((resc_x, resc_y), resultados[2], font=font, fill=font_color, stroke_width=thickness)

                #Texto Respuesta 4
                resd_width, resd_height = draw.textsize(resultados[3], font=font)
                resd_x = x + (w - resd_width) // 2 
                resd_y = y + resd_height + 170
                # Dibujar el texto en la imagen Pillow
                draw.text((resd_x, resd_y), resultados[3], font=font, fill=font_color, stroke_width=thickness)

                #Texto Respuesta 5
                rese_width, rese_height = draw.textsize(resultados[4], font=font)
                rese_x = x + (w - rese_width) // 2
                rese_y = y + rese_height + 220
                # Dibujar el texto en la imagen Pillow
                draw.text((rese_x, rese_y), resultados[4], font=font, fill=font_color, stroke_width=thickness)

                #Texto Reiniciar
                resf_width, resf_height = draw.textsize(despedida, font=font)
                resf_x = x + (w - resf_width) // 2
                resf_y = y + resf_height + 300
                # Dibujar el texto en la imagen Pillow
                draw.text((resf_x, resf_y), despedida, font=font, fill=font_color, stroke_width=thickness)

        # Convertir la imagen Pillow a marco de OpenCV
        frame = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

        # Calcular las coordenadas de la esquina superior izquierda de la ventana
        window_x = (screen_width - frame.shape[1]) // 2
        window_y = (screen_height - frame.shape[0]) // 2

        cv2.namedWindow('Resultados', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Resultados', frame.shape[1], frame.shape[0])
        cv2.moveWindow('Resultados', window_x, window_y)

        cv2.imshow('Resultados', frame)

        if cv2.waitKey(1) == ord(' '):
            break

    cap.release()
    cv2.destroyAllWindows()
    return reiniciar


def comprobar_evento(texto):
    if(texto != None):
        substrings = ["reiniciar", "salir"]
        for substring in substrings:
            if substring in texto:
                return substring, True
        return "f", False
    else:
        return "f", False
