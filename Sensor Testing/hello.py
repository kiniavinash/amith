import RPi.GPIO as V
import time
V.setmode(V.BOARD)
V.setup(7, V.OUT)
try:
	while True:
		V.output(7,True)
		time.sleep(1)
		V.output(7,False)
		time.sleep(1)
except KeyboardInterrupt:
	print 'Thank you!'	
	V.cleanup()
