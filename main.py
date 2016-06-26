#-*- coding: utf8 -*-
__author__ = 'Veltarn'
import time
import datetime

from settings import climax

import RPi.GPIO as GPIO

from libs.Clock import Clock
from libs.Timer import Timer

from Sensors.Temperature import TemperatureSensor
from Sensors.Exceptions import TemperatureSensorException, DHTTimeoutError, DHTChecksumError
from Sensors.DHT11 import HumiditySensor, Humidity
from Models.DHT11Model import HumiditySensorModel, HumiditySensorRecord

from Models.TemperatureModel import TemperatureModel

def tprint(msg):
	now = datetime.datetime.now()
	str_datetime = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')

	message = "[" + str_datetime + "]: " + msg
	print(message)

def update():
	pass

def listsensors():
	tprint("Channels:")
	tprint("\tDHT11 (humidity): " + str(climax.dht11_channel))
	tprint("\tTemperature uses /sys/bus/w1/devices/")

#todo Encapsulate the GPIO management inside a class
def initGPIO():
	tprint("Starting GPIO")
	GPIO.setmode(GPIO.BOARD)

def closeGPIO():
	tprint("Stopping GPIO")
	GPIO.cleanup()
#===========================

#todo Exporter cette chose dans une classe plus propre!
def daemon():
	tprint("Starting Climax Daemon")
	sleep_time = 10
	listsensors()
	initGPIO()

	temperatureModel = TemperatureModel()
	temperatureSensor = TemperatureSensor()
	humiditySensor = HumiditySensor(climax.dht11_channel)
	humidityModel = HumiditySensorModel()

	try:
		while True:
			tprint("Getting temperature data")
			try:
				temperature = temperatureSensor.get_temperature()
			except TemperatureSensorException as e:
				tprint(e.message)
			else:
				tprint("It's " + str(temperature.celsius()) + "C")
				tprint("Writing temperature on the DB")
				affected_rows = temperatureModel.insert(temperature)
				tprint("Wrote " + str(affected_rows) + " line(s))")

			tprint("Getting humidity data")

			humidity_ok = False
			max_tries = 50
			i = 0
			#Looping while the sensor has not returned a correct set of data OR the loop reached the timeout
			while not humidity_ok and i <= max_tries:
				try:
					humidity = humiditySensor.read_sensor()
				except DHTTimeoutError as e:
					tprint(e.message + "\nRetry in 1 second")
					time.sleep(1)
					i += 1
				except DHTChecksumError as e:
					tprint(e.message + "\nRetry in 1 second")
					time.sleep(1)
					i += 1
				else:
					humidity_ok = True
					tprint("Ambiant humidity is " + str(humidity.value))
					tprint("Humidity has been read correctly")
					tprint("Writing it on the DB")
					affected_rows = humidityModel.insert(humidity)

			if not humidity_ok and i >= max_tries:
				tprint("Cannot get humidity data")

			tprint("End of data harvest, going to bed for 10 seconds")
			time.sleep(sleep_time)
	except KeyboardInterrupt:
		tprint("Received Interrupt signal, stopping daemon")
		closeGPIO()
		tprint("Done, see ya")

def main():
    temperatureModel = TemperatureModel()
    temperatureSensor = TemperatureSensor()

    try:
        while True:
            try:
                temp = temperatureSensor.get_temperature()
            except TemperatureSensorException as exception:
                tprint("An error occured while reading temperature")
                tprint("\t" + exception.message)
            else:
                tprint(temp.celsius())
                temperatureModel.insert(temp)
            finally:
                time.sleep(10)
    except KeyboardInterrupt:
        pass
    finally:
        temperatures = temperatureModel.load_all()

        tprint("Displaying " + str(len(temperatures)))

        for i, data in enumerate(temperatures):
            date = data[2];
            tprint("[" + datetime.datetime.strftime(date, "%Y-%m-%d %H:%M:%S") + "] " + str(data[1]/1000.0))

def main2():
	daemon()

if __name__ == "__main__":
    #main()
	main2()
