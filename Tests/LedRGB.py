#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

LED_ROUGE = 19
LED_BLEUE = 18
LED_VERTE = 21

GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED_ROUGE, GPIO.OUT)
GPIO.setup(LED_VERTE, GPIO.OUT)
GPIO.setup(LED_BLEUE, GPIO.OUT)

ledGauche = GPIO.PWM(LED_ROUGE, 50)
ledMilieu = GPIO.PWM(LED_VERTE, 50)
ledDroite = GPIO.PWM(LED_BLEUE, 50)

ledGauche.start(0)
ledMilieu.start(0)
ledDroite.start(0)

try:
	while 1:
		for dc in range(0, 101, 1):
			ledGauche.ChangeDutyCycle(dc)
			time.sleep(0.01)
		time.sleep(0.3)
		for dc in range(0, 101, 1):
			ledMilieu.ChangeDutyCycle(dc)
			time.sleep(0.01)
		time.sleep(0.3)
		for dc in range(0, 101, 1):
			ledDroite.ChangeDutyCycle(dc)
			time.sleep(0.01)
		time.sleep(0.01)
		for dc in range(100, -1, -1):
			ledGauche.ChangeDutyCycle(dc)
			time.sleep(0.01)
		time.sleep(0.2)
		for dc in range(100, -1, -1):
			ledMilieu.ChangeDutyCycle(dc)
			time.sleep(0.01)
		time.sleep(0.2)
		for dc in range(100, -1, -1):
			ledDroite.ChangeDutyCycle(dc)
			time.sleep(0.01)
		time.sleep(0.01)
except KeyboardInterrupt:
	pass

ledGauche.stop()
ledMilieu.stop()
ledDroite.stop()
GPIO.cleanup()
