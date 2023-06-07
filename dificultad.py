import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from threading import Thread, Event
from speech import reconocimiento_de_voz, getTextoReconocido

dificultad = None
evento = Event()

def seleccionar_dificultad(dificultad_seleccionada, ventana):
    global dificultad
    dificultad = dificultad_seleccionada
    ventana.destroy()


def interfaz_dificultad():
    global dificultad

    def comprobar_evento():
        global titulo_tema
        global dificultad
        if evento.is_set():
            texto_reconocido = getTextoReconocido()
            result = comprobarNivel(texto_reconocido)
            if (result == True):
                ventana.destroy()
            else:
                h1.start()
        else:
            ventana.after(100, comprobar_evento)

    ventana = tk.Tk()
    ventana.title("Elegir Dificultad")
    ventana.resizable(0, 0)

    ancho_pantalla = ventana.winfo_screenwidth()
    altura_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla // 2) - (600 // 2)
    y = (altura_pantalla // 2) - (300 // 2)
    ventana.geometry(f"600x300+{x}+{y}")

    # Cargar la imagen
    imagen = Image.open("Imagenes/micro.png")
    imagen = imagen.resize((100, 100), Image.ANTIALIAS)
    icono = ImageTk.PhotoImage(imagen)

    #Texto
    texto = "Diga por voz o pulse la dificultad:"

    label_titulo = ttk.Label(ventana, text=texto)
    label_titulo.pack(pady=10)

    label_icono = ttk.Label(ventana, image=icono)
    label_icono.pack()

    # Estilo para los botones
    estilo_boton = ttk.Style()
    estilo_boton.configure("TButton", font=("Arial", 12))

    frame_botones = ttk.Frame(ventana, padding=20)
    frame_botones.pack(side="bottom", padx=20, pady=30)

    boton_facil = ttk.Button(frame_botones, text="Fácil", command=lambda: seleccionar_dificultad("0", ventana))
    boton_facil.pack(side="left", padx=20)
    boton_dificil = ttk.Button(frame_botones, text="Difícil", command=lambda: seleccionar_dificultad("1", ventana))
    boton_dificil.pack(side="left", padx=20)

    #Iniciar la hebra de speech 
    h1 = Thread(target=reconocimiento_de_voz, args=(evento,))
    h1.start()

    #Comprobar evento
    comprobar_evento()

    ventana.mainloop()

    return dificultad

def comprobarNivel(texto_reconocido):    
    global dificultad
    if(texto_reconocido != None):
        substring = "dif"
        if substring in texto_reconocido.lower():
            dificultad = 0
        else:
            dificultad = 1
            return True
        return False
    else:
        return False

