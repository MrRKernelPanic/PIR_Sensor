import time
#import pygame
import RPi.GPIO as GPIO

#pygame.init()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_PIR = 4
print "Pir sensor running!!!"
GPIO.setup(GPIO_PIR,GPIO.IN)

num = 0
status0 = 0
status1 = 0

try:
	print "Waiting for sensor..."
	while GPIO.input(GPIO_PIR)==1:
		status0 = 0
	print "Ready to start"
	while True:
		status0 = GPIO.input(GPIO_PIR)
		if status0 == 1 and status1 == 0:
			num=num+1
			print "Hooray detected something!", num, "time/s"
			status1=1
		elif status0==0 and status1==1:
			print "Ready to start"
			status1=0
		time.sleep(0.01)
except KeyboardInterrupt:
	print "Exit!"
	GPIO.cleanup() 
