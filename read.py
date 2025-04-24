'''
This file is responsible for reading the information transmitted by the Arduino Uno over serial. Please set correct COM port for your Arduino
'''

import serial
port = 'COM4'
#^^^ HERE CHANGE PORT TO THE ONE CORRESPONDING TO YOUR ARDUINO UNO
unoSerial = serial.Serial(port=port, baudrate=9600)

def getSerial():
    unoRead = unoSerial.readline()

    #decode string to multiple pots
    pots = str(unoRead, 'UTF-8').split(":")
    return pots

def masterVolume():
    return float(getSerial()[0])
def pot1():
    return float(getSerial()[1])
def pot2():
    return float(getSerial()[2])
def pot3():
    return float(getSerial()[3])
def pot4():
    #substracting '\r\n' from serial
    return float(getSerial()[4][:-2])