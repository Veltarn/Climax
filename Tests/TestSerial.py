__author__ = 'Veltarn'
import serial

def readlineCR(port):
    rv = ""
    while True:
        ch = port.read()
        rv += ch
        if ch == '\r' or ch == '':
            return rv

port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=5.0)

try:
    while True:
        rcv = readlineCR(port)
        print(rcv)

except KeyboardInterrupt:
    pass
