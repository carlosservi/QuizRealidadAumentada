import interfazInicial
import interfazTema
import quiz
import dificultad

def main():
    nombre = interfazInicial.interfaz_inicial()
    if(nombre != None):
        nombre_tema = interfazTema.interfaz_tema()
        dif = dificultad.interfaz_dificultad()
        array_aciertos = quiz.ejecutar_quiz(nombre_tema)
        #print(array_aciertos)


if __name__ == "__main__":
    main()