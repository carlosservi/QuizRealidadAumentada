import interfazInicial
import interfazTema
import quiz

def main():
    nombre = interfazInicial.interfaz_inicial()
    if(nombre != None):
        nombre_tema, dificultad = interfazTema.interfaz_tema()
        #print(dificultad)
        array_aciertos = quiz.ejecutar_quiz(nombre_tema)
        #print(array_aciertos)


if __name__ == "__main__":
    main()