
   #READ

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Joel Gonsalves 112")
    id, text = reader.read()
    print(id)
    print(text)
finally:
    GPIO.cleanup()


    #WRITE

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Joel Gonsalves 112")
    text = input('Enter now: ')
    reader.write(text)
    print("Written")
finally:
    GPIO.cleanup()


#1-24
#2-23
#3-19
#4-21
#5-x
#6-6
#7-22
#8-1

