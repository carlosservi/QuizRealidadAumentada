import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import dificultad


# Variable global para almacenar el título del tema seleccionado
titulo_tema = None
dif = None


def interfaz_tema():
    global titulo_tema
    global dif

    def tema_wrapper(nombre_seccion, ventana):
        global titulo_tema
        global dif
        titulo_tema = nombre_seccion
        #dif = dificultad.interfaz_dificultad()
        ventana.destroy()
    
    ventana = tk.Tk()
    ventana.title("Elegir Tema")
    ventana.resizable(0, 0)

    # Obtener el ancho y la altura de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    altura_pantalla = ventana.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    x = (ancho_pantalla // 2) - (800 // 2)
    y = (altura_pantalla // 2) - (600 // 2)

    # Configurar las coordenadas de la ventana
    ventana.geometry(f"800x600+{x}+{y}")

    # Iconos y títulos de las secciones
    iconos = [
        tk.PhotoImage(file="Imagenes/animales.png"),
        tk.PhotoImage(file="Imagenes/paises.png"),
        tk.PhotoImage(file="Imagenes/profesiones.png"),
        tk.PhotoImage(file="Imagenes/deportes.png"),
        tk.PhotoImage(file="Imagenes/micro.png"),
        tk.PhotoImage(file="Imagenes/instrumentos.png"),
        tk.PhotoImage(file="Imagenes/cuerpo.png"),
        tk.PhotoImage(file="Imagenes/transporte.png"),
        tk.PhotoImage(file="Imagenes/rio.png")
    ]
    titulos = [
        "Animales",
        "Paises",
        "Profesiones",
        "Deportes",
        "Diga un tema",
        "Instrumentos",
        "Cuerpo",
        "Transporte",
        "Rios"
    ]

    # Crear las secciones
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            icono = iconos[index]
            titulo = titulos[index]
            crear_seccion(ventana, i, j, icono, titulo, tema_wrapper)

    # Ejecutar la interfaz gráfica
    ventana.mainloop()

    return titulo_tema, dif


def crear_seccion(ventana, fila, columna, icono, titulo, tema_wrapper):
    frame = ttk.LabelFrame(ventana, padding="10 20 10 10")
    frame.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")
    
    label_icono = ttk.Label(frame, image=icono)
    label_icono.pack()
    
    label_titulo = ttk.Label(frame, text=titulo)
    label_titulo.pack(pady=5)
    if titulo != "Diga un tema":
        boton_seccion = ttk.Button(frame, text="Ir al Quiz", command=lambda nombre_seccion=titulo: tema_wrapper(nombre_seccion,ventana))
        boton_seccion.pack(pady=10)

    # Configurar el sistema de gestión de geometría grid para que la sección se expanda
    ventana.grid_rowconfigure(fila, weight=1)
    ventana.grid_columnconfigure(columna, weight=1)