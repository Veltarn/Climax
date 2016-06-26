__author__ = 'Veltarn'

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
port_number = 7
GPIO.setup(port_number, GPIO.IN)

def onRising(channel):
    '''
    Called whenever the hall sensor is triggered
    :param channel: Number of the channel
    :return:
    '''
    print("Event on " + str(channel))

def onFalling(channel):
    '''
    Called whenever the hall sensors stop detecting something
    :param channel:
    :return:
    '''
    print("Nothing to detect")

def main():

    GPIO.add_event_detect(port_number, GPIO.RISING, callback=onRising)

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == "__main__":
    main()