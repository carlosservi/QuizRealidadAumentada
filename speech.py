import speech_recognition as sr
from unidecode import unidecode
from threading import Thread, Event, Lock

# Variable para almacenar el texto reconocido
texto_reconocido = None
# Cerrojo para garantizar acceso exclusivo a la variable de texto_reconocido
cerrojo = Lock()
# Evento para indicar cuando se ha reconocido un texto
evento = Event()

def reconocimiento_de_voz():
    global texto_reconocido, cerrojo, evento
    # Crea un objeto Recognizer para el reconocimiento de voz
    r = sr.Recognizer()
    while True:
        # Abre el micrófono como fuente de audio
        with sr.Microphone() as source:
            # Ajusta el nivel de ruido ambiental
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Escuchando...")
            # Escucha el audio desde el micrófono
            audio = r.listen(source)
            try:
                # Reconoce el audio utilizando el servicio de reconocimiento de Google
                texto = r.recognize_google(audio, language='es-ES')
                print(f"Reconocido: {texto}")
                # Establece el evento para indicar que se ha reconocido un texto
                evento.set()
                # Almacena el texto reconocido en la variable global y asegurando con el cerrojo
                with cerrojo:
                    #Convierte el texto a minúscula
                    texto = texto.lower()
                    #Elimina los acentos del texto
                    texto_reconocido = unidecode(texto)
            except Exception as e:
                print("Error:" + str(e))

