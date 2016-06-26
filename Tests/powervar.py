import RPi.GPIO as GPIO
import time

LED = 21

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)

ledObj = GPIO.PWM(LED, 50)

ledObj.start(0)

try:
	while 1:
		for dc in range(0, 101, 1):
			ledObj.ChangeDutyCycle(dc)
			time.sleep(0.01)
		
		for dc in range(100, -1, -1):
			ledObj.ChangeDutyCycle(dc)
			time.sleep(0.01)
except KeyboardInterrupt:
	pass
finally:
	ledObj.stop()
	GPIO.cleanup()

