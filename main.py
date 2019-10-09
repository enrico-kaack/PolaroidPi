from  Adafruit_Thermal import *
from PIL import Image

import RPi.GPIO as GPIO
import time

printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

def shutterPressed(channel):
    print("button pressed")
    GPIO.output(25, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(25, GPIO.LOW)

    printer.test()


GPIO.add_event_detect(10,GPIO.RISING,callback=shutterPressed)


