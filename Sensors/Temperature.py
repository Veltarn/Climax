__author__ = 'Veltarn'

import os
import time
from Sensors.Exceptions import TemperatureSensorException
from Sensors.AbstractSensor import AbstractSensor


class TemperatureSensor(AbstractSensor):
    def __init__(self):
        self.sensor_path_resource = "/sys/bus/w1/devices/28-03164475c0ff/w1_slave"

        print("Starting DS18B20 Sensor")
        self.init_sensor()

    def init_sensor(self):
        # Activating the appropriate modules in case they are not
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

    def check_sensor_file(self):
        '''
            Checks if the sensor file exists
            Throws an exception otherwise
        '''
        if not os.path.isfile(self.sensor_path_resource):
            raise TemperatureSensorException("Cannot open serial port at " + self.sensor_path_resource + ", file does not exists")

    def read_sensor_data(self):
        try:
            self.check_sensor_file()
        except TemperatureSensorException:
            raise
        else:
            sensor_file = open(self.sensor_path_resource, 'r')
            data = sensor_file.readlines()
            sensor_file.close()

            return data

    def get_temperature(self):
        try:
            data = self.read_sensor_data()
        except TemperatureSensorException:
            print("An error occured while reading temperature")
            raise
        else:
            # YES is stored in this variable if the sensor is ready
            sensor_readiness = data[0].strip()[-3:]

            if sensor_readiness != "YES":
                #Wait 200ms before calling that method again
                time.sleep(0.2)

                # This exception block is needed to handle the exception
                try:
                    return self.get_temperature()
                except TemperatureSensorException:
                    print("An error occured while reading temperature")
                    raise
            else:
                position = data[1].find("t=")
                #position + 2 to ignore 't='
                temp_string = data[1].strip()[position+2:]
                temperature = Temperature(float(temp_string))

                return temperature


class Temperature:
    def __init__(self, raw_temp):
        self.raw_temperature = raw_temp

    def celsius(self):
        return float(self.raw_temperature) / 1000.0

    def fahrenheit(self):
        return self.celsius() * 9.0 / 5.0 + 32.0

    def raw_value(self):
        return self.raw_temperature



