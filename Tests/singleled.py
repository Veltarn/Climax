import RPi.GPIO as GPIO
import time

LED = 23

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)

try:
	while 1:
		GPIO.output(LED, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(LED, GPIO.LOW)
		time.sleep(0.5)
		print("test")
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
