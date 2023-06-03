import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

dificultad = None

def seleccionar_dificultad(dificultad_seleccionada, ventana):
    global dificultad
    dificultad = dificultad_seleccionada
    ventana.destroy()


def interfaz_dificultad():
    global dificultad

    ventana = tk.Tk()
    ventana.title("Elegir Dificultad")
    ventana.resizable(0, 0)

    ancho_pantalla = ventana.winfo_screenwidth()
    altura_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla // 2) - (600 // 2)
    y = (altura_pantalla // 2) - (300 // 2)
    ventana.geometry(f"600x300+{x}+{y}")

    #icono = tk.PhotoImage(file="Imagenes/micro.png")
    texto = "Diga por voz o pulse la dificultad:"
    
    # label_icono = ttk.Label(ventana, image=icono)
    # label_icono.pack()
    label_titulo = ttk.Label(ventana, text=texto)
    label_titulo.pack(pady=10)

    # Estilo para los botones
    estilo_boton = ttk.Style()
    estilo_boton.configure("TButton", font=("Arial", 12))

    frame_botones = ttk.Frame(ventana, padding=20)
    frame_botones.pack(side="bottom", padx=20, pady=20)

    boton_facil = ttk.Button(frame_botones, text="Fácil", command=lambda: seleccionar_dificultad("Fácil", ventana))
    boton_facil.pack(side="left", padx=5)
    boton_medio = ttk.Button(frame_botones, text="Medio", command=lambda: seleccionar_dificultad("Medio", ventana))
    boton_medio.pack(side="left", padx=5)
    boton_dificil = ttk.Button(frame_botones, text="Difícil", command=lambda: seleccionar_dificultad("Difícil", ventana))
    boton_dificil.pack(side="left", padx=5)

    ventana.mainloop()

    return dificultad

