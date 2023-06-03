import cv2
import imutils
from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
import numpy as np
import screeninfo
from preguntas import get_preguntas, get_respuestas
import random
import time

def ejecutar_quiz(tema):
    cap = cv2.VideoCapture(0)

    # Obtener las dimensiones de la pantalla
    screen_info = screeninfo.get_monitors()[0]
    screen_width = screen_info.width
    screen_height = screen_info.height

    # Configuración del texto a mostrar
    font_path = "Font/RubikDistressed-Regular.ttf"
    font_size = 36
    font_color = (255, 255, 255)  # Color blanco
    thickness = 0
    font_size2 = 70

    # Cargar la fuente personalizada
    font = ImageFont.truetype(font_path, font_size)
    font2 = ImageFont.truetype(font_path, font_size2)

    # Detector de rostros
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cont = 0
    i = random.randint(0, 9)
    text = get_preguntas(tema, i)
    respuesta = None
    tiempo_total = 10
    inicio = time.time()
    cuenta_regresiva = 10
    resultado = False

    array_aciertos = []
    array_preguntas = []
    array_preguntas.append(i)

    while True and cont < 5:
        #Gestionar respuesta y tiempo
        if respuesta or cuenta_regresiva == 0:
            resultado = False
            if respuesta == get_respuestas(tema,i):
                array_aciertos.append(True)
                text = "CORRECTO"
                resultado = True
            elif respuesta != None:
                array_aciertos.append(False)
                text = "INCORRECTO"
                resultado = True
                
            cont = cont + 1

            if resultado == False:
                while i in array_preguntas:
                    i = random.randint(0, 9)
                array_preguntas.append(i)
                text = get_preguntas(tema, i)
                inicio = time.time()

        # Restar el tiempo transcurrido al tiempo total para obtener la cuenta regresiva
        tiempo_transcurrido = int(time.time() - inicio)
        cuenta_regresiva = tiempo_total - tiempo_transcurrido

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
            # Calcular las coordenadas superiores izquierdas del texto para que esté centrado en el rostro
            text_width, text_height = draw.textsize(text, font=font)
            text_x = x + (w - text_width) // 2
            text_y = y - text_height

            # Dibujar el texto en la imagen Pillow
            if resultado == False:
                draw.text((text_x, text_y), text, font=font, fill=font_color, stroke_width=thickness)
            else:
                draw.text((text_x, text_y), text, font=font2, fill=font_color, stroke_width=thickness)

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

    cap.release()
    cv2.destroyAllWindows()
    return array_aciertos
