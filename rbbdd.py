tablas_sql = [
    """
    CREATE TABLE Tematicas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255)
    )
    """,
    """
    CREATE TABLE Preguntas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_tematica INT,
        nivel INT,
        pregunta TEXT,
        r_correcta VARCHAR(1),
        FOREIGN KEY (id_tematica) REFERENCES Tematicas(id)
    )
    """,
    """
    CREATE TABLE Respuestas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_pregunta INT,
        opcion VARCHAR(1),
        respuesta TEXT,
        es_correcta TINYINT(1),
        FOREIGN KEY (id_pregunta) REFERENCES Preguntas(id)
    )
    """
]

tematicas = [
    'Animales',
    'Paises',
    'Profesiones',
    'Deportes',
    'Instrumentos',
    'Cuerpo',
    'Transporte',
    'Rios'
]

opciones_correctas = {
    "Animales": {
        0: ['c', 'd', 'd', 'a', 'd'],
        1: ['b', 'b', 'a', 'b', 'd']
    },
    "Paises": {
        0: ['a', 'a', 'c', 'c', 'a'],
        1: ['a', 'a', 'b', 'd', 'b']
    },
    "Profesiones": {
        0: ['c', 'd', 'b', 'c', 'a'],
        1: ['b', 'a', 'a', 'b', 'd']
    },
    "Colores": {
        0: ['c', 'a', 'd', 'b', 'd'],
        1: ['a', 'b', 'b', 'c', 'a']
    },
    "Deportes": {
        0: ['d', 'c', 'a', 'b', 'a'],
        1: ['c', 'd', 'b', 'a', 'b']
    },
    "Instrumentos": {
        0: ['a', 'c', 'd', 'b', 'c'],
        1: ['a', 'd', 'b', 'a', 'c']
    },
    "Cuerpo": {
        0: ['d', 'a', 'b', 'a', 'c'],
        1: ['a', 'b', 'c', 'b', 'd']
    },
    "Transporte": {
        0: ['b', 'd', 'c', 'a', 'a'],
        1: ['d', 'c', 'd', 'a', 'b']
    },
    "Rios": {
        0: ['d', 'c', 'a', 'b', 'a'],
        1: ['a', 'c', 'b', 'a', 'd']
    }
}

preguntas = {
    "Animales": {
        0: [
        "Cuál es el animal más grande del mundo?",
        "Qué animal vuela y hace miel?",
        "Cuál es el animal más rápido del mundo?",
        "Qué animal tiene una joroba en la espalda?",
        "Qué animal es conocido por su trompa larga?"
        ],
        1: [
        "Qué animal tiene una melena y ruge?",
        "Cuál es el animal que puede nadar y volar?",
        "Qué animal tiene rayas negras y blancas?",
        "Qué animal tiene manchas negras y blancas?",
        "Cuál es el animal que hiberna durante el invierno?"
        ]
    },
    "Paises": {
        0: [
        "Cuál es el país más poblado del mundo?",
        "En qué país se encuentra la Torre Eiffel?",
        "Cuál es el país más grande de América Latina?",
        "En qué país se encuentra la Gran Muralla China?",
        "Cuál es el país más pequeño del mundo?"
        ],
        1: [
        "En qué país se encuentra la ciudad de Roma?",
        "Cuál es el país más grande de África?",
        "En qué país se encuentra el Taj Mahal?",
        "Cuál es el país más grande de Europa?",
        "En qué país se encuentra la ciudad de Atenas?"
        ]
    },
    "Profesiones": {
        0: [
        "Cuál es la profesión que se encarga de cuidar los dientes?",
        "Qué profesión se dedica a construir edificios?",
        "Qué profesión se ocupa de defender a las personas acusadas?",
        "Qué profesión se dedica a cuidar y tratar a los animales enfermos?",
        "Cuál es la profesión que se encarga de apagar incendios?"
        ],
        1: [
        "Qué profesión se dedica a enseñar en las escuelas?",
        "Cuál es la profesión que se ocupa de pilotar aviones?",
        "Qué profesión se dedica a diseñar puentes y carreteras?",
        "Cuál es la profesión que se encarga de la salud de las personas?",
        "Qué profesión se dedica a escribir noticias?"
        ]
    },
    "Deportes": {
        0: [
        "En qué deporte se utiliza una raqueta para golpear una pelota?",
        "Cuál es el deporte más popular en Estados Unidos?",
        "En qué deporte se lanza un disco hacia una diana?",
        "Cuál es el deporte que se juega en una pista y se corre en círculos?",
        "En qué deporte se utiliza un palo para golpear una bola en un hoyo?"
        ],
        1: [
        "Cuál es el deporte en el que se lucha cuerpo a cuerpo en un tatami?",
        "En qué deporte se utiliza una tabla para deslizarse sobre las olas?",
        "Cuál es el deporte que se juega sobre hielo y con un disco?",
        "En qué deporte se corre, se salta y se lanza una jabalina?",
        "Cuál es el deporte en el que dos equipos compiten por marcar goles?"
        ]
    },
    "Instrumentos": {
        0: [
        "Cuál es el instrumento de cuerda que se toca con un arco?",
        "Qué instrumento de percusión se toca con las manos?",
        "Instrumento de viento que se toca soplando y tiene llaves?",
        "Qué instrumento de teclado tiene 88 teclas?",
        "Instrumento de viento que se toca soplando y tiene tres válvulas?"
        ],
        1: [
        "Qué instrumento de percusión se toca con baquetas y tiene platillos?",
        "Instrumento de cuerda que se toca con los dedos y tiene trastes?",
        "Instrumento que se toca soplando con una boquilla y tiene teclas?",
        "Cuál es el instrumento de cuerda que es más grande que el violín?",
        "Instrumento que se toca con las manos y tiene forma de media luna?"
        ]
    },
    "Cuerpo": {
        0: [
        "Cuál es el órgano que bombea la sangre?",
        "Qué parte del cuerpo contiene los dientes?",
        "Cuál es el hueso largo de la parte superior del brazo?",
        "Qué parte del cuerpo se utiliza para oler?",
        "Cuál es el órgano principal del sistema nervioso?"
        ],
        1: [
        "Qué parte del cuerpo contiene los pulmones?",
        "Cuál es el hueso más largo del cuerpo?",
        "Qué parte del cuerpo contiene el estómago?",
        "Cuál es el músculo principal en la parte posterior de la pierna?",
        "Qué parte del cuerpo se utiliza para ver?"
        ]
    },
    "Transporte": {
        0: [
        "Qué medio de transporte se utiliza para volar en el aire?",
        "Medio de transporte que se utiliza para navegar en el agua?",
        "Qué medio de transporte se utiliza para viajar sobre rieles?",
        "Medio de transporte que se utiliza en ciudad y tiene dos ruedas?",
        "Medio de transporte personal que tiene cuatro ruedas?"
        ],
        1: [
        "Medio de transporte que tiene dos ruedas y un motor?",
        "Medio de transporte para navegar en el agua y más pequeño que un barco?",
        "Medio de transporte que es tirado por caballos?",
        "Medio de transporte recreativo marítimo?",
        "Medio de transporte con tres ruedas para niños?"
        ]
    },
    "Rios": {
        0: [
        "Cuál es el río más largo de España?",
        "Cuál es el río que atraviesa Madrid?",
        "Cuál es el río que separa España de Portugal?",
        "Cuál es el río que pasa por Sevilla?",
        "Río que nace en los Picos de Europa y desemboca en el Cantábrico?"
        ],
        1: [
        "Cuál es el río que pasa por Barcelona?",
        "Río que forma la frontera natural entre España y Francia?",
        "Cuál es el río que atraviesa Zaragoza?",
        "Cuál es el río que atraviesa Valencia?",
        "Río que nace en Cazorla y desemboca en el Mar Mediterráneo?"
        ]
    }
}

respuestas = {
    "Animales": {
        0: [
            ["Elefante", "Delfín", "Ballena", "León"],
            ["Mariposa", "Colibrí", "Gorrión", "Abeja"],
            ["Leopardo", "Águila", "Tortuga", "Guepardo"],
            ["Camello", "Jirafa", "Cebra", "Caballo"],
            ["Rinoceronte", "Tigre", "Gorila", "Elefante"]
        ],
        1: [
            ["Cebra", "León", "Tigre", "Guepardo"],
            ["Pingüino", "Pato", "Aguila", "Gaviota"],
            ["Tigre", "Cebra", "Cocodrilo", "Panda"],
            ["Jirafa", "Cebra", "Cocodrilo", "Tigre"],
            ["Ballena", "Panda", "León Marino", "Oso"]
        ]
    },
    "Paises": {
        0: [
            ["China", "India", "Estados Unidos", "Rusia"],
            ["Francia", "Italia", "Alemania", "España"],
            ["México", "Argentina", "Brasil", "Colombia"],
            ["Japón", "Corea del Sur", "China", "India"],
            ["Vaticano", "Mónaco", "Nauru", "San Marino"]
        ],
        1: [
            ["Italia", "Grecia", "España", "Francia"],
            ["Argelia", "Egipto", "Sudáfrica", "Nigeria"],
            ["Pakistán", "India", "Bangladesh", "Nepal"],
            ["Alemania", "Francia", "España", "Rusia"],
            ["Italia", "Grecia", "Turquía", "Egipto"]
        ]
    },
    "Profesiones": {
        0: [
            ["Médico", "Enfermero", "Dentista", "Farmacéutico"],
            ["Arquitecto", "Ingeniero", "Electricista", "Constructor"],
            ["Juez", "Abogado", "Detective", "Policía"],
            ["Biólogo", "Zoólogo", "Veterinario", "Fontanero"],
            ["Bombero", "Policía", "Paramédico", "Rescatista"]
        ],
        1: [
            ["Profesor", "Maestro", "Educador", "Instructor"],
            ["Piloto", "Astronauta", "Controlador", "Azafata"],
            ["Ingeniero", "Arquitecto", "Topógrafo", "Urbanista"],
            ["Enfermero", "Médico", "Farmacéutico", "Odontólogo"],
            ["Escritor", "Editor", "Redactor", "Periodista"]
        ]
    },
    "Colores": {
        0: [
            ["Verde", "Azul", "Morado", "Amarillo"],
            ["Rojo", "Naranja", "Rosado", "Violeta"],
            ["Azul", "Negro", "Marrón", "Verde"],
            ["Naranja", "Amarillo", "Blanco", "Rosa"],
            ["Amarillo", "Verde", "Azul", "Naranja"]
        ],
        1: [
            ["Blanco", "Negro", "Amarillo", "Verde"],
            ["Azul", "Verde", "Negro", "Blanco"],
            ["Rojo", "Azul", "Amarillo", "Verde"],
            ["Morado", "Azul", "Rosa", "Amarillo"],
            ["Azul", "Verde", "Rosado", "Blanco"]
        ]
    },
    "Deportes": {
        0: [
            ["Golf", "Fútbol", "Baloncesto", "Tenis"],
            ["Beisbol", "Fútbol", "Hockey", "Baloncesto"],
            ["Tiro con arco", "Dardos", "Golf", "Frisbee"],
            ["Ciclismo", "Atletismo", "Natación", "Gimnasia"],
            ["Golf", "Tenis", "Críquet", "Béisbol"]
        ],
        1: [
            ["Karate", "Taekwondo", "Judo", "Lucha libre"],
            ["Esquí", "Natación", "Vela", "Surf"],
            ["Patinaje", "Hockey", "Esquí", "Snowboard"],
            ["Atletismo", "Salto altura", "Salto longitud", "Jabalina"],
            ["Rugby", "Fútbol", "Balonmano", "Hockey sobre hielo"]
        ]
    },
    "Instrumentos": {
        0: [
            ["Violín", "Viola", "Cello", "Contrabajo"],
            ["Bongos", "Cajón", "Timba", "Congas"],
            ["Flauta", "Oboe", "Saxofón" ,"Clarinete"],
            ["Órgano", "Piano", "Clavecín", "Sintetizador"],
            ["Trombón", "Tuba", "Trompeta", "Saxofón"]
        ],
        1: [
            ["Batería", "Timbales", "Platillos", "Xilófono"],
            ["Bajo", "Violín", "Ukelele", "Guitarra"],
            ["Flauta travesera", "Saxofón", "Clarinete", "Oboe"],
            ["Violonchelo", "Viola", "Guitarra", "Violín"],
            ["Congas", "Maracas", "Cajón", "Pandero"]
        ]
    },
    "Cuerpo": {
        0: [
            ["Cerebro", "Estómago", "Riñón", "Corazón"],
            ["Boca", "Nariz", "Oído", "Ojo"],
            ["Cúbito", "Húmero", "Radio", "Fémur"],
            ["Nariz", "Oído", "Boca", "Ojo"],
            ["Médula espinal", "Hígado", "Cerebro", "Estómago"]
        ],
        1: [
            ["Pecho", "Estómago", "Hígado", "Riñón"],
            ["Tibia", "Fémur", "Peroné", "Húmero"],
            ["Cabeza", "Pecho", "Abdomen", "Espalda"],
            ["Cuádriceps", "Gemelos", "Bíceps", "Tríceps"],
            ["Oídos", "Boca", "Nariz", "Ojos"]
        ]
    },
    "Transporte": {
        0: [
            ["Helicóptero", "Avión", "Barco", "Coche"],
            ["Kayak", "Submarino", "Hidroavión", "Barco"],
            ["Camión", "Avión", "Tren", "Tranvía"],
            ["Bicicleta", "Patineta", "Coche", "Motocicleta"],
            ["Coche", "Motocicleta", "Bicicleta", "Camión"]
        ],
        1: [
            ["Bicicleta", "Coche", "Patinete", "Motocicleta"],
            ["Yate", "Velero", "Bote", "Submarino"],
            ["Carreta", "Carro", "Torillo", "Carroza"],
            ["Yate", "Barco", "Velero", "Submarino"],
            ["Bicicleta", "Triciclo", "Patineta", "Monopatín"]
        ]
    },
    "Rios": {
        0: [
            ["Duero", "Guadalquivir", "Tajo", "Ebro"],
            ["Sena", "Támesis", "Manzanares", "Rin"],
            ["Miño", "Guadiana", "Duero", "Tajo"],
            ["Ebro", "Guadalquivir", "Duero", "Tajo"],
            ["Sella", "Miño", "Ebro", "Duero"]
        ],
        1: [
            ["Llobregat", "Ebro", "Tajo", "Segura"],
            ["Miño", "Guadiana", "Bidasoa", "Duero"],
            ["Tajo", "Ebro", "Duero", "Guadalquivir"],
            ["Turia", "Miño", "Duero", "Tajo"],
            ["Ebro", "Duero", "Júcar", "Guadalquivir"]
        ]
    }
}
