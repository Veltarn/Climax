#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import random

RED_CHANNEL = 19
BLUE_CHANNEL = 15
GREEN_CHANNEL = 21

GPIO.setmode(GPIO.BOARD)

GPIO.setup(RED_CHANNEL, GPIO.OUT)
GPIO.setup(BLUE_CHANNEL, GPIO.OUT)
GPIO.setup(GREEN_CHANNEL, GPIO.OUT)

redLed = GPIO.PWM(RED_CHANNEL, 50)
blueLed = GPIO.PWM(BLUE_CHANNEL, 50)
greenLed = GPIO.PWM(GREEN_CHANNEL, 50)

redLed.start(0)
greenLed.start(0)
blueLed.start(0)

try:
    while 1:
        rRandom = int(random.random() * 100)
        gRandom = int(random.random() * 100)
        bRandom = int(random.random() * 100)

        print("R: " + str(rRandom))
        print("G: " + str(gRandom))
        print("B: " + str(bRandom))

        redLed.ChangeDutyCycle(rRandom)
        greenLed.ChangeDutyCycle(gRandom)
        blueLed.ChangeDutyCycle(bRandom)
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    redLed.stop()
    greenLed.stop()
    blueLed.stop()
    GPIO.cleanup()
