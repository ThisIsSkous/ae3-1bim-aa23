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
# se recuerda los atributos: nombre, liga, pais, cantJugador
# Equipo 1
nombreEquipo = "SKT"
liga = "MSI"
pais = "Corea"
cantJugador = 7
cadena_sql = """INSERT INTO Equipo (nombre, liga, pais, cantJugador) \
VALUES ('%s', '%s', '%s', %d);""" % (nombreEquipo, liga, pais, cantJugador)

# ejecutar el SQL
cursor.execute(cadena_sql)

# Equipo 2
nombreEquipo = "Fnatic"
liga = "MSI"
pais = "Suecia"
cantJugador = 7
cadena_sql = """INSERT INTO Equipo (nombre, liga, pais, cantJugador) \
VALUES ('%s', '%s', '%s', %d);""" % (nombreEquipo, liga, pais, cantJugador)

# ejecutar el SQL
cursor.execute(cadena_sql)

# Equipo 3
nombreEquipo = "DRX"
liga = "MSI"
pais = "Corea"
cantJugador = 7
cadena_sql = """INSERT INTO Equipo (nombre, liga, pais, cantJugador) \
VALUES ('%s', '%s', '%s', %d);""" % (nombreEquipo, liga, pais, cantJugador)

# ejecutar el SQL
cursor.execute(cadena_sql)

# Equipo 4
nombreEquipo = " Lyon Gaming"
liga = "MSI"
pais = "Argentina"
cantJugador = 7
cadena_sql = """INSERT INTO Equipo (nombre, liga, pais, cantJugador) \
VALUES ('%s', '%s', '%s', %d);""" % (nombreEquipo, liga, pais, cantJugador)

# ejecutar el SQL
cursor.execute(cadena_sql)


# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
