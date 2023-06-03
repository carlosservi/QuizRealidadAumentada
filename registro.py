import os
import cv2
import tkinter as tk
from tkinter import simpledialog, messagebox
import imutils
import time

def registrarse():
    # Solicitar el nombre al usuario
    nombre = simpledialog.askstring("Nombre", "Ingrese su nombre")

    if nombre and nombre.strip():
        # Crear la ruta de la carpeta con el nombre
        nombre_path = 'Data/' + nombre.strip()
        if not os.path.exists(nombre_path):
            os.makedirs(nombre_path)

        # Obtener el ancho y la altura de la pantalla
        ventana = tk.Tk()
        ventana.withdraw()
        ancho_pantalla = ventana.winfo_screenwidth()
        altura_pantalla = ventana.winfo_screenheight()
        ventana.destroy()

        # Inicializar la captura de video desde la webcam
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            messagebox.showerror("Error", "No se puede abrir la cámara")
            return

        # Configurar el temporizador para capturar una imagen cada segundo
        tiempo_inicial = time.time()
        intervalo = 2.0

        # Capturar imágenes mientras se actualiza la ventana de la webcam
        count = 1
        mensaje = "Foto 1 realizada"
        while True:
            ret, frame = cap.read()

            if not ret:
                messagebox.showerror("Error", "No se puede leer el frame")
                return

            frame = imutils.resize(frame, width=500)

            if count == 2:
                mensaje = "Foto 2 realizada"
            elif count == 3:
                mensaje = "Foto 3 realizada"
            cv2.putText(frame, mensaje, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            
            cv2.imshow('WEBCAM', frame)
            # Mover la ventana al centro de la pantalla
            cv2.moveWindow('WEBCAM', (ancho_pantalla // 2) - (500 // 2), (altura_pantalla // 2) - (500 // 2))

            if time.time() - tiempo_inicial > intervalo:
                # Guardar la imagen en la carpeta con el nombre
                imagen_path = os.path.join(nombre_path, f"imagen{count}.jpg")
                cv2.imwrite(imagen_path, frame)

                count += 1
                tiempo_inicial = time.time()

                if count > 3:
                    break

            if cv2.waitKey(1) == ord(' '):
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Completado", "Registro satisfactorio")
    return

    
