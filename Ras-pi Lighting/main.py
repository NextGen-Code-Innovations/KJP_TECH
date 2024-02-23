import os
import RPi.GPIO as gpio
import time

print("Imported files and applications...")

# main setup
gpio.setup(2, gpio.out)
gpio.setup(3, gpio.out)
gpio.setup(4, gpio.out)

# working area 
gpio.output(2, gpio.HIGH)
