#! /usr/bin/env python

# Importamos el conector de MySQL
import mysql.connector
import time

# Variable con la configuracion de la conexion
config_mysql = {
    'user'    : 'root',
    'password': '',
    'host'    : 'localhost',
    'database': 'datos_iot',
}

# conectamos al servidor MySql
conector = mysql.connector.connect(**config_mysql)

# cursor, clase para el manejo del SQL ???
cursor = conector.cursor()

# Creamos la consulta SQL
query = ("SELECT id, dato, fecha FROM datos_sensor")

# Ejecutamos la consula SQL
cursor.execute(query)

# Mostramos todos los datos de la consulta
for (id, dato, fecha) in cursor:
    print("ID: " + str(id) + ", Dato: " + str(dato) + ", Fecha: " + str(fecha))

# Cerramos cursor
cursor.close()

# Cerramos la conexion
conector.close()
