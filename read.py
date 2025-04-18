'''
This file is responsible for reading the information transmitted by the PiPico over serial.

In further development this function will decode multiple inputs from the transmitted string.
'''
import serial

ser = serial.Serial(port='COM3', baudrate=9600)

def getValue():
    value = ser.readline()
    read = str(value, 'UTF-8')

    volumeValue = float(read[0:4])
    return volumeValue