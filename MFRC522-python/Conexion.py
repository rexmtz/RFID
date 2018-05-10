#! /usr/bin/env python

# Importamos el conector de MySQL
import mysql.connector

def Conexion():
  config_mysql = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'datos_iot',
  }
  conector = mysql.connector.connect(**config_mysql)
  return conector


# Variable con la configuracion de la conexion
#config_mysql = {
#    'user'    : 'root',
#    'password': '',
#    'host'    : 'localhost',
#    'database': 'datos_iot',
#}

# conectamos al servidor MySql

# cursor, clase para el manejo del SQL ???

# Creamos la consulta SQL

# Mostramos todos los datos de la consulta
#for (id, dato, fecha) in cursor:
##    print("ID: " + id + ", Dato: " + dato + ", Fecha: " + fecha)

# Cerramos cursor

# Cerramos la conexion
