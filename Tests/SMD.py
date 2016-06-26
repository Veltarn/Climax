import random
import time
import RPi.GPIO as GPIO

def micro_sleep(ticks):
	time.sleep(ticks/1000.0)

def get_interpolation_step(duration, amount_to_interpolate):
	return amount_to_interpolate / (duration * 30)


red_port = 23
green_port = 7
blue_port = 21

GPIO.setmode(GPIO.BOARD)

GPIO.setup(red_port, GPIO.OUT)
GPIO.setup(green_port, GPIO.OUT)
GPIO.setup(blue_port, GPIO.OUT)

pwm_red = GPIO.PWM(red_port, 0.5)
pwm_green = GPIO.PWM(green_port, 0.5)
pwm_blue = GPIO.PWM(blue_port, 0.5)

try:
	while True:
		target_red = 0
		target_green = 0
		target_blue = 0
	
		new_red = random.randint(0, 255)
		new_green = random.randint(0, 255)
		new_blue = random.randint(0, 255)

		delta_red = target_red - new_red
		delta_green = target_green - new_green
		delta_blue = target_blue - new_blue
	
		inter_red = get_interpolation_step(1, delta_red)
		inter_green = get_interpolation_step(1, delta_green)
		inter_blue = get_interpolation_step(1, delta_blue)
		
		done = False
		
		current_red = target_red
		current_green = target_green
		current_blue = target_blue

		while not done:
			current_red += inter_red
			current_green += inter_green
			current_blue += inter_blue

			pcent_red = abs((current_red * 100) / new_red)				
			pcent_blue = abs((current_blue * 100) / new_blue)
			pcent_green = abs((current_green * 100) / new_green)
		
			pwm_red.ChangeDutyCycle(pcent_red)
			pwm_green.ChangeDutyCycle(pcent_green)
			pwm_blue.ChangeDutyCycle(pcent_blue)

			if pcent_red >= 100:
				done = True
			
			d
			
		target_red = new_red
                target_green = new_green
                target_blue = new_blue
	
except KeyboardInterrupt:
	print("Cleaning GPIO states")
	pwm_red.stop()
	pwm_blue.stop()
	pwm_green.stop()
	GPIO.cleanup()
	print("Done, bye bye")
