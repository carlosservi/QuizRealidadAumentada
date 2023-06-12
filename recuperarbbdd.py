import bbdd
    
#Recuperación de base de datos
bbdd.conexion()
bbdd.limpiarBaseDeDatos()
bbdd.recuperarTablas()
bbdd.recuperarTematicas()
bbdd.recuperarPreguntas()
bbdd.cerrarConexion()