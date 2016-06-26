__author__ = 'Veltarn'

import RPi.GPIO as GPIO

portNumber = input("Type the GPIO port\n > ")

print("GPIO port is " + str(portNumber))

# Init the GPIO

GPIO.setmode(GPIO.BOARD)

print(GPIO.getmode())

GPIO.setup(portNumber, GPIO.IN)

try:
    while True:
        print("Current GPIO state: " + str(GPIO.gpio_function(portNumber)))
        print(GPIO.input(portNumber))
except KeyboardInterrupt:
    pass

GPIO.cleanup()