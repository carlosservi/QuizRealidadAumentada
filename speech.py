import speech_recognition as sr

texto_reconocido = None

def reconocimiento_de_voz(evento):
    global texto_reconocido
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        try:
            texto_reconocido = r.recognize_google(audio, language='es')
            evento.set()
            return texto_reconocido

        except sr.UnknownValueError:
            print("No se pudo reconocer el audio")
            return None

        except sr.RequestError as e:
            print("Error al solicitar resultados del servicio de reconocimiento de voz:", str(e))
            return None

def getTextoReconocido():
    return texto_reconocido
