from  Adafruit_Thermal import *
from PIL import Image

printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout=5)

i = Image.open("img.png")
printer.printImage(i)