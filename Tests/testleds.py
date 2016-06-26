#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

LED_DROITE = 11
LED_MILIEU = 9
LED_GAUCHE = 10

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_DROITE, GPIO.OUT)
GPIO.setup(LED_MILIEU, GPIO.OUT)
GPIO.setup(LED_GAUCHE, GPIO.OUT)

ledGauche = GPIO.PWM(LED_GAUCHE, 50)
ledMilieu = GPIO.PWM(LED_MILIEU, 50)
ledDroite = GPIO.PWM(LED_DROITE, 50)

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
