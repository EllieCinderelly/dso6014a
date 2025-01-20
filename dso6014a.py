import pyvisa as visa
import sys
import spidev

# Intended use for this file is SSH control to RPi SPi outputs and controlling the Agilent DSO6014A 
# windows python ssh -> rpi spidev and pyvisa-py
# This file goes on the pi
# windows IVI drivers for DSO6014A seem to be very deprecated. Pyvisa-py on rpi4 is proving best here


ID = 'USB0::2391::5924::MY45007512::0::INSTR'

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 9600
spi.mode = 0

def measure(ID,words):

    rm = visa.ResourceManager('@py')
    oscope = rm.open_resource(ID)
    oscope.timeout = None
    instrument_ID = oscope.query('*IDN?')
    print('Instrument Info:\n%s' % (instrument_ID))
    spi_send(words)
    oscope.close()
    rm.close()

def spi_send(spi_arr):
    to_send = []*len(spi_arr)
    for i in range(len(spi_arr)):
            print(spi_arr)
            print(spi_arr[i])
            print(int(spi_arr[i],16))
            to_send.append(int(spi_arr[i],16))
    
    print(to_send)    
    spi.xfer(to_send)
    print('Sent %s' % (spi_arr))


if __name__ == '__main__':

    n = []
    for i in range(1, len(sys.argv), 1):
        n.append(sys.argv[i])

    measure(ID,n)