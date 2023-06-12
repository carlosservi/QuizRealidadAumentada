import interfazInicial
import interfazTema
import quiz
import dificultad
import bbdd
from threading import Thread
import speech
import resultados



def main():    
    try:
        reiniciar = True
        nombre = interfazInicial.interfaz_inicial()
        if(nombre != None):
            h1 = Thread(target=speech.reconocimiento_de_voz)
            h1.daemon = True
            h1.start()
            while reiniciar:
                nombre_tema = interfazTema.interfaz_tema()
                if nombre_tema == None:
                    break
                dificultad.interfaz_dificultad()
                dif = dificultad.dificultad
                if dif == None:
                    break
                bbdd.conexion()
                preguntas = bbdd.consultar_preguntas(nombre_tema, dif)
                respuestas = bbdd.consultar_respuestas(nombre_tema, dif)
                letras = bbdd.consultar_letras_correctas(nombre_tema, dif)
                bbdd.cerrarConexion()
                if preguntas == None or respuestas == None or letras == None:
                    break
                correctas = quiz.ejecutar_quiz(preguntas, respuestas, letras)
                if correctas == None or len(correctas) < 5:
                    break
                reiniciar = resultados.resultados(correctas, nombre)
    except Exception as e:
        print("Error en la ejecución del programa:" + str(e))
    
    
    
    


if __name__ == "__main__":
    main()