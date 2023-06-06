import mysql.connector
import rbbdd as r

con = None

def conexion():
    global con 
    con = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="123",
        database="quiz"
    )

def recuperarTablas():
    global con
    cursor = con.cursor()
    for tablas in r.tablas_sql:
        cursor.execute(tablas)
    con.commit()

def recuperarTematicas():
    global con
    cursor = con.cursor()
    for tematica in r.tematicas:
        cursor.execute("INSERT INTO Tematicas (nombre) VALUES (%s)", (tematica,))
    con.commit()

def recuperarPreguntas():
    global con
    cursor = con.cursor()
    insert_question_query = """
                    INSERT INTO Preguntas (id_tematica, nivel, pregunta, r_correcta)
                    VALUES ((SELECT id FROM Tematicas WHERE nombre = %s), %s, %s, %s)
                """
    insert_answer_query = """
                        INSERT INTO Respuestas (id_pregunta, opcion, respuesta, es_correcta)
                        VALUES (%s, %s, %s, %s)
                    """
    for tematica in r.tematicas:
        for nivel in range(2):
            for i, pregunta_text in enumerate(r.preguntas[tematica][nivel]):
                # Inserción de preguntas
                cursor.execute(insert_question_query, (tematica, nivel, pregunta_text, r.opciones_correctas[tematica][nivel][i]))
                question_id = cursor.lastrowid
                # Inserción the respuestas
                for j, respuesta_text in enumerate(r.respuestas[tematica][nivel][i]):
                    es_correcta = 1 if r.opciones_correctas[tematica][nivel][i] == chr(97 + j) else 0
                    cursor.execute(insert_answer_query, (question_id, chr(97 + j), respuesta_text, es_correcta))
    
    con.commit()

def cerrarConexion():
    global con
    con.close()

def mostrarTablas():
    global con
    cursor = con.cursor()
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'quiz'")

    # Obtener todos los resultados de la consulta
    resultados = cursor.fetchall()

    # Recorrer los resultados
    for fila in resultados:
        print(fila[0])

def limpiarBaseDeDatos():
    global con
    cursor = con.cursor()

    # Eliminar todas las tuplas de las tablas
    cursor.execute("DELETE FROM Respuestas")
    cursor.execute("DELETE FROM Preguntas")
    cursor.execute("DELETE FROM Tematicas")

    # Eliminar las tablas
    cursor.execute("DROP TABLE IF EXISTS Respuestas")
    cursor.execute("DROP TABLE IF EXISTS Preguntas")
    cursor.execute("DROP TABLE IF EXISTS Tematicas")

    con.commit()

def consultar_preguntas(tematica, nivel):
    global con
    cursor = con.cursor()
    query = """
        SELECT pregunta
        FROM Preguntas p
        INNER JOIN Tematicas t ON p.id_tematica = t.id
        WHERE t.nombre = %s AND p.nivel = %s
    """
    cursor.execute(query, (tematica, nivel))
    preguntas = cursor.fetchall()
    preguntas = [pregunta[0] for pregunta in preguntas]
    return preguntas

def consultar_respuestas(tematica, nivel):
    global con
    cursor = con.cursor()
    query = """
        SELECT opcion, respuesta
        FROM Respuestas r
        INNER JOIN Preguntas p ON r.id_pregunta = p.id
        INNER JOIN Tematicas t ON p.id_tematica = t.id
        WHERE t.nombre = %s AND p.nivel = %s
    """
    cursor.execute(query, (tematica, nivel))
    respuestas = cursor.fetchall()
    return respuestas

def consultar_letras_correctas(tematica, nivel):
    global con
    cursor = con.cursor()
    query = """
        SELECT r_correcta
        FROM Preguntas p
        INNER JOIN Tematicas t ON p.id_tematica = t.id
        WHERE t.nombre = %s AND p.nivel = %s
    """
    cursor.execute(query, (tematica, nivel))
    letras_correctas = cursor.fetchall()
    letras_correctas = [letra[0] for letra in letras_correctas]
    return letras_correctas