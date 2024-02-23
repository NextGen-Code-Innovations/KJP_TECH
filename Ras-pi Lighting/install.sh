#!/bin/bash

#install the gpio packages
print -p "Installing python dev packages"

sudo apt-get install python-dev
print -p "Installed Dev Packages"

print -p "Installing gpio packages"
sudo apt-get install python-rpi.gpio
print -p "Installed gpio packages"

print -p "DONE!"
