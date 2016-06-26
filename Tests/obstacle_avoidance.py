import time
import RPi.GPIO as GPIO

avoid_sensor = 23

def main():
	GPIO.setmode(GPIO.BOARD)
	
	GPIO.setup(avoid_sensor, GPIO.IN)
	
	try:
		while True:
			if GPIO.input(avoid_sensor) == 0:
				print("Obstacle detected!")
				time.sleep(0.1)
	except KeyboardInterrupt:
		print("Releasing GPIO resources")
		GPIO.cleanup()

if __name__ == "__main__":
	main()
