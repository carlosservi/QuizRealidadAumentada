import interfazInicial
import interfazTema
import quiz
import dificultad
import bbdd
from threading import Thread
import speech
import resultados



def main():
    #Recuperación de base de datos
    # bbdd.conexion()
    # bbdd.limpiarBaseDeDatos()
    # bbdd.recuperarTablas()
    # bbdd.recuperarTematicas()
    # bbdd.recuperarPreguntas()
    # bbdd.cerrarConexion()
    
    #Flujo normal de la aplicación
    try:
        reiniciar = True
        nombre = interfazInicial.interfaz_inicial()
        if(nombre != None):
            h1 = Thread(target=speech.reconocimiento_de_voz)
            h1.daemon = True
            h1.start()
            while reiniciar:
                nombre_tema = interfazTema.interfaz_tema()
                dificultad.interfaz_dificultad()
                dif = dificultad.dificultad
                bbdd.conexion()
                preguntas = bbdd.consultar_preguntas(nombre_tema, dif)
                respuestas = bbdd.consultar_respuestas(nombre_tema, dif)
                letras = bbdd.consultar_letras_correctas(nombre_tema, dif)
                bbdd.cerrarConexion()
                correctas = quiz.ejecutar_quiz(preguntas, respuestas, letras)
                reiniciar = resultados.resultados(correctas)
    except Exception as e:
        print("Error en la ejecución del programa:" + str(e))
    
    
    
    


if __name__ == "__main__":
    main()