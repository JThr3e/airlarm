import httplib2
import time
import RPi.GPIO as io

io.setmode(io.BCM)
io.setup(3, io.OUT)
 
while True:
	http = httplib2.Http()
	content = http.request("http://airlarm.herokuapp.com/state")[1]
	#print(content.decode())
	if "armed" == content.decode():
		io.output(3,1)
		print "armed"
	else:
		io.output(3,0)
		print "disarmed" 
	time.sleep(0.5)
