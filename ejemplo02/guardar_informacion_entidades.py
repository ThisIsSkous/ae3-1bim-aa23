"""
    Guarda información en las entidades en la base de datos
"""

from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear una cadena que almacene la sentencia de ingreso de información
# se recuerda los atributos: nombre, apellido, equipo, 
# 1 Jugador
nombre = "Lee Sang"
apellido = "hyeok"
equipo = "SKT"
cadena_sql = """INSERT INTO Jugador (nombre, apellido, equipo) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, equipo )

# ejecutar el SQL
cursor.execute(cadena_sql)

# 2 Jugador
nombre = "Jose"
apellido = "Deodo"
equipo = "Fnatic"
cadena_sql = """INSERT INTO Jugador (nombre, apellido, equipo) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, equipo )

# ejecutar el SQL
cursor.execute(cadena_sql)

# 3 Jugador
nombre = "Keira"
apellido = "Smith"
equipo = "DRX"
cadena_sql = """INSERT INTO Jugador (nombre, apellido, equipo) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, equipo )

# ejecutar el SQL
cursor.execute(cadena_sql)

# 4 Jugador
nombre = "Kim Hyuk"
apellido = "kyu "
equipo = "Lyon Gaming"
cadena_sql = """INSERT INTO Jugador (nombre, apellido, equipo) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, equipo)

# ejecutar el SQL
cursor.execute(cadena_sql)


# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
