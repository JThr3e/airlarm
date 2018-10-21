#Code for Airlarm home safety system


import mraa
import time

#Is Airlarm armed?
status = mraa.Gpio(33)
status.dir(mraa.DIR_IN)

#Should we turn on the airhorm?
opto = mraa.Gpio(29)
opto.dir(mraa.DIR_OUT)

#Was motion detected?
motion = mraa.Gpio(31)
motion.dir(mraa.DIR_IN)

#Always run the code to continually check the status of the system
while True:
  armed = int(status.read())
  print "Armed? 1 = yes 0 = no"
  print armed
  time.sleep(0.5)

  #If Airlarm is armed
  while armed:

    #If motion was detected, we want to turn on the optocoupler and in
    #turn the airhorn
    airhorn = int(motion.read())
    print "Turn on airhorn? Was motion detected? 1 = yes 0 = no"
    print airhorn
    if(airhorn == 1):
      print "Turning on opto"
      opto.write(1)
      time.sleep(0.1)
      opto.write(0)
      time.sleep(0.1)
      opto.write(1)
      time.sleep(0.1)
      opto.write(0)
      time.sleep(0.1)
      opto.write(1)
      time.sleep(0.1)
      opto.write(0)
    else:
      print "Turning off opto"
      opto.write(0)

    #Recheck whether the system is armed or not
    armed = int(status.read())
    print "New status"
    print armed
    time.sleep(0.75)
