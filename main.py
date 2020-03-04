import os 
import subprocess
from thermalprinter import *
from PIL import Image
from picamera import PiCamera
from gpiozero import Button
from signal import pause
import os.path
from threading import Thread, Lock

printer = ThermalPrinter(port="/dev/serial0", baudrate=9600)
camera = PiCamera()
button = Button(5, hold_time = 2)

photo_path = "/home/pi/photos"
mutex = Lock()


def foto_and_print():
	if mutex.locked():
		return
	mutex.acquire()
	try:
		print("Foto and print.")
		camera.capture("image.jpg")
		i = Image.open("image.jpg")
		i = i.rotate(90, expand = True)
		width, height = i.size
		percentage = float(384/float(width))
		i = i.resize((int(384), int(percentage * float(height))), Image.ANTIALIAS)
		printer.image(i)
		printer.feed(4)

		# Save image to folder
		for j in range(500):
			filename = photo_path + "/" + str(j) + ".jpg"
			if os.path.isfile(filename):
				pass
			else:
				i.save(filename)
				break
	except:
		print("Could not take foto and print")

	finally:
		mutex.release()
		

def print_last(): 
	if mutex.locked():
		return
	mutex.acquire()
	try:
		print("Print Last")
		biggest = -1

		for file in os.listdir(photo_path):
			file = file.split(".")[0]
			try:
				if int(file) > biggest:
					biggest = int(file)
			except:
				#print("Not numerical file name " + file)
				pass

		if not biggest == -1:
			i = Image.open(photo_path + "/" + str(biggest) + str(".jpg"))
			printer.image(i)
			printer.feed(4)

	except:
		print("Could not print last photo")

	finally:
		mutex.release()
		

def shutdown():
	os.system("sudo shutdown now")


button.when_released = foto_and_print
button.when_held = print_last #shutdown

pause()