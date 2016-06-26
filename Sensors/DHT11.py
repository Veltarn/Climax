__author__ = 'Veltarn'

import RPi.GPIO as GPIO

from Sensors.utils import micro_sleep
from Sensors.Exceptions import GPIONotInitializeError, DHTTimeoutError, DHTChecksumError
from Sensors.AbstractSensor import AbstractSensor


class HumiditySensor(AbstractSensor):
    def __init__(self, dht11Port):
        self.channel = dht11Port
        self.last_value = None

        if not GPIO.getmode():
            raise GPIONotInitializeError()

        print("Starting DHT11 sensor")

    def read_sensor(self):
        #DHT11 timeout
        DHT_MAX_COUNT = 32000
        DHT_PULSES = 41

        pulse_count = [0] * (DHT_PULSES * 2)

        GPIO.setup(self.channel, GPIO.OUT)

        #Send a high voltage signal to the DHT
        GPIO.output(self.channel, GPIO.HIGH)
        micro_sleep(500)
        GPIO.output(self.channel, GPIO.LOW)

        micro_sleep(20)
        GPIO.setup(self.channel, GPIO.IN)

        count = 0

        #Wait for DHT pin to be low
        while GPIO.input(self.channel):
            count += 1
            if count >= DHT_MAX_COUNT:
                raise DHTTimeoutError()

        for i in xrange(0, DHT_PULSES * 2, 2):
            # Count how long pin is low
            while not GPIO.input(self.channel):
                pulse_count[i] += 1
                if pulse_count[i] >= DHT_MAX_COUNT:
                    raise DHTTimeoutError()

            # Count how long pin is high
            while GPIO.input(self.channel):
                pulse_count[i + 1] += 1
                if pulse_count[i+1] >= DHT_MAX_COUNT:
                    raise DHTTimeoutError()

        threshold = 0
        # Compute the average low pulses to make a threshold between what could be a 0 and a 1
        for i in xrange(2, DHT_PULSES * 2, 2):
            threshold += pulse_count[i]

        threshold /= DHT_PULSES - 1

        data = [0] * 5
        for i in xrange(3, DHT_PULSES * 2, 2):
            index = int((i - 3) / 16)
            data[index] <<= 1
            if pulse_count[i] >= threshold:
                data[index] |= 1

        #Verifying checksum
        if data[4] == ((data[0] + data[1] + data[2] + data[3]) & 0xFF):
            humidity = Humidity(data[0])
            self.last_value = humidity
            return humidity
        else:
            raise DHTChecksumError()

class Humidity:
    def __init__(self, data):
        self.value = data