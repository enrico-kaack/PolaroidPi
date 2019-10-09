from  Adafruit_Thermal import *
from PIL import Image

import RPi.GPIO as GPIO
import time

shutterNumber = 21
menuNumber = 35

printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(shutterNumber, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(menuNumber, GPIO.OUT, initial=GPIO.LOW)

def shutterPressed(channel):
	print("menu button pressed")
    i = Image.open("img.png")
	printer.printImage(i)

def menuPressed(channel):
	print("button pressed")
    GPIO.output(menuNumber, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(menuNumber, GPIO.LOW)

    printer.test()


GPIO.add_event_detect(shutterNumber,GPIO.RISING,callback=shutterPressed)
PIO.add_event_detect(menuNumber,GPIO.RISING,callback=menuPressed)
