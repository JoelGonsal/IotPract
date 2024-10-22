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




