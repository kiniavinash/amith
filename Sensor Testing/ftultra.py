import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
trig = 16
echo = 18

##print 'Distance Measurement in progress'

gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)

gpio.output(trig,False)

##print 'Waiting for the sensor to settle'

##time.sleep(2)

gpio.output(trig,True)
time.sleep(0.00001)
gpio.output(trig,False)

while gpio.input(echo)==0:
	start = time.time()

while gpio.input(echo)==1:
	end = time.time()

duration = end-start

speed = 34600

dist = duration * speed * 0.5

dist = round(dist,2)

print dist , 'cm'

gpio.cleanup()
