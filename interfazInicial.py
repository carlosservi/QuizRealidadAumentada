import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from login import loguearse
from registro import registrarse
from threading import Thread

#Variable global para almacenar el nombre del usuario
nombre=None

#Función para registrarse
def registrarse_usuario():
    registrarse()

#Función de la interfaz inicial con la lógica
def interfaz_inicial():
    global nombre

    ventana = tk.Tk()
    ventana.title("Aplicación de Reconocimiento Facial")
    ventana.resizable(0,0)

    # Obtener el ancho y la altura de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    altura_pantalla = ventana.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    x = (ancho_pantalla // 2) - (600 // 2)
    y = (altura_pantalla // 2) - (500 // 2)

    # Configurar las coordenadas de la ventana4
    ventana.geometry(f"600x500+{x}+{y}")

    # Cargar la imagen
    imagen = Image.open("Imagenes/silueta.jpg")
    imagen = imagen.resize((400, 400), Image.ANTIALIAS)
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Crear el widget Label para mostrar la imagen
    label_imagen = ttk.Label(ventana, image=imagen_tk)
    label_imagen.pack()

    # Estilo para los botones
    estilo_boton = ttk.Style()
    estilo_boton.configure("TButton", font=("Arial", 12))

    # Marco para los botones
    marco_botones = ttk.Frame(ventana)
    marco_botones.pack(side="bottom", padx=20, pady=30)

    # Botón de loguearse
    boton_loguearse = ttk.Button(marco_botones, text="Loguearse", command=lambda: login(ventana), style="TButton")
    boton_loguearse.pack(side="left", padx=20)

    # Botón de registrarse
    boton_registrarse = ttk.Button(marco_botones, text="Registrarse", command=registrarse_usuario, style="TButton")
    boton_registrarse.pack(side="left", padx=20)

    #Iniciar la hebra de logueo    
    h1 = Thread(target=login(ventana))
    h1.start()
    
    # Ejecutar la interfaz gráfica
    ventana.mainloop()
    return nombre
    
#Función para loguearse
def login(ventana):
    global nombre
    nombre = loguearse()
    if nombre != None:
        ventana.destroy()