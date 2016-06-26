# -*- coding: utf8 -*-
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)

sys.path.append(PARENT_DIR)

from Models.DHT11Model import HumiditySensorRecord, HumiditySensorModel


import RPi.GPIO as GPIO
from Sensors.DHT11 import HumiditySensor, Humidity
from Sensors.Exceptions import GPIONotInitializeError, DHTChecksumError, DHTTimeoutError
import time

def main():
    GPIO.setmode(GPIO.BOARD)

    humiditySensor = HumiditySensor(23)
    humidityModel = HumiditySensorModel()
    try:
        while True:
            try:
                humidity = humiditySensor.read_sensor()
            except DHTTimeoutError:
                print("DHT Sensor timeouted, delaying next call")
                time.sleep(2)
            except DHTChecksumError as e:
                print(e.message)
            else:
                print("Current humidity: " + str(humidity.value))
                humidityModel.insert_value(humidity)
            finally:
                time.sleep(2)
    except KeyboardInterrupt:
        GPIO.cleanup()

    records = humidityModel.load_all()

    print(records)
if __name__ == "__main__":
    main()
