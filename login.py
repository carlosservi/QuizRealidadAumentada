import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import cv2
import face_recognition
import os

def loguearse():
    encodings_registrados = []
    nombres_registrados = []

    nombres_usuarios = os.listdir("Data")
    if not os.path.exists("Data"):
        print("No se puede abrir el archivo")

    for nombre_usuario in nombres_usuarios:
        ruta_usuario = os.path.join("Data", nombre_usuario)
        nombres_imagenes = os.listdir(ruta_usuario)
        for nombre_imagen in nombres_imagenes:
            ruta_imagen = os.path.join(ruta_usuario, nombre_imagen)
            imagen_registrada = face_recognition.load_image_file(ruta_imagen)
            encoding_registrado = face_recognition.face_encodings(imagen_registrada)[0]
            encodings_registrados.append(encoding_registrado)
            nombres_registrados.append(nombre_usuario)

    # Inicializar la cámara
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        messagebox.showerror("Error", "No se puede abrir la cámara")
        return None

    while True:
        # Capturar un fotograma de la cámara
        ret, frame = cap.read()

        # Detectar las caras en el fotograma
        ubicaciones = face_recognition.face_locations(frame)
        encodings = face_recognition.face_encodings(frame, ubicaciones)

        # Comparar los encodings de las caras detectadas con los encodings registrados
        for encoding in encodings:
            coincidencias = face_recognition.compare_faces(encodings_registrados, encoding)

            if True in coincidencias:
                indice = coincidencias.index(True)
                nombre_registrado = nombres_registrados[indice]
                cap.release()
                cv2.destroyAllWindows()
                # Mostrar el cuadro de mensaje
                messagebox.showinfo("Reconocido", f'Hola {nombre_registrado}')
                return nombre_registrado

        break
    # Liberar los recursos
    cap.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("No Reconocido", "Lo siento no estás registrado")
    return None


