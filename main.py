import interfazInicial
import interfazTema
import quiz
import dificultad
import bbdd

def main():
     nombre = interfazInicial.interfaz_inicial()
     if(nombre != None):
         nombre_tema = interfazTema.interfaz_tema()
         dif = dificultad.interfaz_dificultad()
         bbdd.conexion()
         preguntas = bbdd.consultar_preguntas(nombre_tema, dif)
         respuestas = bbdd.consultar_respuestas(nombre_tema, dif)
         letras = bbdd.consultar_letras_correctas(nombre_tema, dif)
         bbdd.cerrarConexion()
         quiz.ejecutar_quiz(preguntas, respuestas, letras)
    
    # bbdd.limpiarBaseDeDatos()
    # bbdd.recuperarTablas()
    # bbdd.recuperarTematicas()
    # bbdd.recuperarPreguntas()
    


if __name__ == "__main__":
    main()