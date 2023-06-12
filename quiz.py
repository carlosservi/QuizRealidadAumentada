import cv2
import imutils
from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
import numpy as np
import screeninfo
import time
from threading import Thread, Event
import speech as sp

respuesta = None

#Función principal del Quiz
def ejecutar_quiz(preguntas, respuestas, letras_correctas):
    # Inicializar las variables
    correctas = []
    sp.evento.clear()
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

    # Inicializar el contador de preguntas y respuestas
    cont = 0
    contres = 0
    texto = preguntas[cont]
    resa = "A. "+respuestas[contres][1]
    resb = "B. "+respuestas[contres+1][1]
    resc = "C. "+respuestas[contres+2][1]
    resd = "D. "+respuestas[contres+3][1]

    # Inicializar el texto de correcto e incorrecto y contadores de tiempo
    text = ""
    correcto = "Correcto!"
    incorrecto = "Incorrecto!"
    total_correcto = 2
    cuenta_correcto = 2
    ini_correcto = time.time()

    # Inicializar el tiempo y declarar el tiempo total y la cuenta regresiva
    tiempo_total = 21
    cuenta_regresiva = 21
    inicio = time.time()

    comprobacion = False

    while True and cont < 5:
        #Gestionar respuesta y tiempo
        if (sp.evento.is_set() or cuenta_regresiva == 0) and comprobacion == False:
            comprobacion = True
            with sp.cerrojo:
                respuesta = comprobar_evento(sp.texto_reconocido)
            if respuesta != None:
                if respuesta == letras_correctas[cont]:
                    text = correcto
                    correctas.append(True)
                else:
                    text = incorrecto
                    correctas.append(False)
                ini_correcto = time.time()
                cuenta_regresiva = 21
        elif comprobacion == True and cuenta_correcto == 0:
            cont = cont+1
            if cont < len(preguntas):
                texto = preguntas[cont]
                contres = contres+4
                resa = "A. "+respuestas[contres][1]
                resb = "B. "+respuestas[contres+1][1]
                resc = "C. "+respuestas[contres+2][1]
                resd = "D. "+respuestas[contres+3][1]
                inicio = time.time()
                comprobacion = False
                cuenta_correcto = 2
                sp.evento.clear()
            else:
                break
    
        # Restar el tiempo transcurrido al tiempo total para obtener la cuenta regresiva
        if comprobacion == False:
            tiempo_transcurrido = int(time.time() - inicio)
            cuenta_regresiva = tiempo_total - tiempo_transcurrido
        else:
            tiempo_transcurrido = int(time.time() - ini_correcto)
            cuenta_correcto = total_correcto - tiempo_transcurrido

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

        # Calcular las coordenadas superiores izquierdas de los números para que esté en la esquina inferior derecha
        cuenta = f"{cuenta_regresiva}"
        cuenta_width, cuenta_height = draw.textsize(cuenta, font=font2)
        cuenta_x = frame.shape[1] - cuenta_width - 10
        cuenta_y = frame.shape[0] - cuenta_height - 10
        # Dibujar la cuenta regresiva en la imagen Pillow
        draw.text((cuenta_x, cuenta_y), cuenta, font=font2, fill=font_color, stroke_width=thickness)
        
        for (x, y, w, h) in faces:
            # Calcular las coordenadas superiores izquierdas de los textos para que estén centrados con el rostro
            if comprobacion==True:
                #Texto Respuesta
                texta_width, texta_height = draw.textsize(text, font=font2)
                texta_x = x + (w - texta_width) // 2
                texta_y = y - texta_height
                # Dibujar el texto en la imagen Pillow
                draw.text((texta_x, texta_y), text, font=font2, fill=font_color, stroke_width=thickness)
            else:
                #Texto Pregunta
                text_width, text_height = draw.textsize(texto, font=font)
                text_x = x + (w - text_width) // 2
                text_y = y - text_height
                # Dibujar el texto en la imagen Pillow
                draw.text((text_x, text_y), texto, font=font, fill=font_color, stroke_width=thickness)

                #Texto Respuesta a
                resa_width, resa_height = draw.textsize(resa, font=font)
                resa_x = x - resa_width
                resa_y = y + resa_height + 20
                # Dibujar el texto en la imagen Pillow
                draw.text((resa_x, resa_y), resa, font=font, fill=font_color, stroke_width=thickness)

                #Texto Respuesta b
                resb_width, resb_height = draw.textsize(resb, font=font)
                resb_x = x - resb_width
                resb_y = y + resb_height + 80
                # Dibujar el texto en la imagen Pillow
                draw.text((resb_x, resb_y), resb, font=font, fill=font_color, stroke_width=thickness)

                #Texto Respuesta c
                resc_width, resc_height = draw.textsize(resc, font=font)
                resc_x = x + w
                resc_y = y + resc_height + 20
                # Dibujar el texto en la imagen Pillow
                draw.text((resc_x, resc_y), resc, font=font, fill=font_color, stroke_width=thickness)

                #Texto Respuesta d
                resd_width, resd_height = draw.textsize(resd, font=font)
                resd_x = x + w
                resd_y = y + resd_height + 80
                # Dibujar el texto en la imagen Pillow
                draw.text((resd_x, resd_y), resd, font=font, fill=font_color, stroke_width=thickness)

        # Convertir la imagen Pillow a marco de OpenCV
        frame = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

        # Calcular las coordenadas de la esquina superior izquierda de la ventana
        window_x = (screen_width - frame.shape[1]) // 2
        window_y = (screen_height - frame.shape[0]) // 2

        cv2.namedWindow('QUIZ', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('QUIZ', frame.shape[1], frame.shape[0])
        cv2.moveWindow('QUIZ', window_x, window_y)

        cv2.imshow('QUIZ', frame)

        if cv2.waitKey(1) == ord(' '):
            break

    # Liberar los recursos
    cap.release()
    cv2.destroyAllWindows()
    return correctas

#Función para comprobar la respuesta
def comprobar_evento(texto):
    if(texto != None):
        substrings = ["a", "b", "c", "d"]
        for substring in substrings:
            if substring in texto:
                return substring
        return "f"
    else:
        return "f"
