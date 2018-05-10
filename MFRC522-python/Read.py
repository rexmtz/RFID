#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import time

reader = SimpleMFRC522.SimpleMFRC522()
blanco =''

try:
  #id = reader.read()
  print("Por Favor Deslisa la Tarjeta")
  id,text = reader.read()
  if(text == blanco):
    print ("Esta Tarjeta Esta Vacia")
  else:
    #print(id)
    print(text)


finally:
  GPIO.cleanup()
