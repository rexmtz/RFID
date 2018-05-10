#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import mysql.connector

reader = SimpleMFRC522.SimpleMFRC522()

class Conexion():
  config_mysql = {
    'user': 'root_rex',
    'password': 'adminrex',
    'host': '192.168.0.5',
    'database': 'datos_iot',
    'port': '50001',
  }
  conector = mysql.connector.connect(**config_mysql)


try:
  text = raw_input('New data:')
  print("Now place your tag to write")
  reader.write(text)
  print ("hi "+text)
  query = "INSERT INTO datos_sensor (id, dato, fecha) VALUES ('','"+ text +"',CURRENT_TIMESTAMP)"
  con = Conexion()
  cursor = con.conector.cursor()
  cursor.execute(query)
  print("Written")
  con.conector.commit()
  cursor.close()
  con.conector.close()

finally:
  GPIO.cleanup()
