import os
import RPi.GPIO as gpio
import time

print("Imported files and applications...")

# main setup
gpio.setup(2, gpio.out)

# working area 