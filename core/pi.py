import RPi.GPIO as GPIO
from datetime import datetime 
import sys, os, subprocess, platform, core.main
import time

tred = "\033[31m"
tgreen = "\033[32m"
tyellow = "\033[33m"
tblue = "\033[36m"
twhite = "\033[37m"


MODE = GPIO.BCM # GPIO.BCM = GPIO Numbering / GPIO.BOARD = Physical Pin Numbering

# BCM Pins based on the relay hat
lightRelay = 5

waterRelay = 6
waterWaitLength = 2 # Seconds for pump to be active

fanRelay = 13
#16
#19
#20
#21
#26
usedPins = []

def init():
	GPIO.setwarnings(False)

def setAsOutput(pin, defaultState):
	GPIO.setmode(MODE) 
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, defaultState)
	usedPins.append(pin)

def setAsInput(pin):
	GPIO.setmode(MODE) 
	GPIO.setup(pin, GPIO.IN)
	usedPins.append(pin)

def clean(pin):
	GPIO.setmode(MODE)
	GPIO.setup(pin, OUT)
	GPIO.output(pin, 0)

def cleanup():
    print("\n[ "+core.main.tblue+"Raspkei"+core.main.twhite+" ] Cleaning GPIO pins...")
    for pins in usedPins:
        GPIO.setup(pins, 0)
    GPIO.cleanup() 
