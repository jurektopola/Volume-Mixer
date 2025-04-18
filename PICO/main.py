'''
CAUTION!!! This is RaspberryPi Pico main.py file, and must not be used on Windows side.
'''

from time import sleep
import sys
from picozero import Pot

dial = Pot(0)

while True:
        cmd = str(dial.value) + "\n"
        sys.stdout.write(cmd)
        #time.sleep(2)
        #print(dial.value)
        sleep(0.2)