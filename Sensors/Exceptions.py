__author__ = 'Veltarn'

class GPIONotInitializeError(Exception):
    def __init__(self):
        msg = "GPIO is not initialized"
        super(GPIONotInitializeError, self).__init__(msg)

class DHTTimeoutError(Exception):
    def __init__(self):
        msg = "DHT sensor didn't responded, timeout occured"
        super(DHTTimeoutError, self).__init__(msg)

class DHTChecksumError(Exception):
    def __init__(self):
        msg = "Incorrect checksum value, probably due to a timeout or a read error"
        super(DHTChecksumError, self).__init__(msg)

class TemperatureSensorException(Exception):
    def __init__(self, message):
        super(TemperatureSensorException, self).__init__(message)