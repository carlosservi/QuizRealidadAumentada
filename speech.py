import speech_recognition as sr
from unidecode import unidecode
from threading import Thread, Event, Lock

texto_reconocido = None
cerrojo = Lock()
evento = Event()

# def reconocimiento_de_voz(evento):
#     global texto_reconocido
#     r = sr.Recognizer()
#     while True:
#         print("Entro en la hebra")
#         with sr.Microphone() as source:
#             r.adjust_for_ambient_noise(source, duration=0.5)
#             audio = r.listen(source)
#             try:
#                 print("Reconociendo...")
#                 texto_reconocido = r.recognize_google(audio, language='es')
#                 evento.set()
#                 return unidecode(texto_reconocido)

#             except sr.UnknownValueError:
#                 print("No se pudo reconocer el audio")

#             except sr.RequestError as e:
#                 print("Error al solicitar resultados del servicio de reconocimiento de voz:", str(e))

# def reconocimiento_de_voz_quiz(evento):
#     global texto_reconocido
#     print("Entro en la hebra 2")
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source, duration=0.5)
#         audio = r.listen(source)
#         try:
#             print("Reconociendo...")
#             texto_reconocido = r.recognize_google(audio, language='es')
#             substrings = ["a", "b", "c", "d"]
#             for substring in substrings:
#                 if substring in texto_reconocido.lower():
#                     evento.set()
#                     texto_reconocido = substring
#                     return texto_reconocido
#             evento.set()
#             return None

#         except sr.UnknownValueError:
#             print("No se pudo reconocer el audio")
#             return None

#         except sr.RequestError as e:
#             print("Error al solicitar resultados del servicio de reconocimiento de voz:", str(e))
#             return None

# def getTextoReconocido():
#     return unidecode(texto_reconocido)

def reconocimiento_de_voz():
    global texto_reconocido, cerrojo, evento
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Escuchando...")
            audio = r.listen(source)
            try:
                texto = r.recognize_google(audio, language='es-ES')
                print(f"Reconocido: {texto}")
                evento.set()
                with cerrojo:
                    texto = texto.lower()
                    texto_reconocido = unidecode(texto)
            except Exception as e:
                print("Error:" + str(e))

