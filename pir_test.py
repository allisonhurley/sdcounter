import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

# now we'll define two threaded callback functions  
# these will run in another thread when our events are detected  
def my_callback(channel):  
    print "falling edge detected on 17"  
  
def my_callback2(channel):  
    print "falling edge detected on 23"  
    
# when a falling edge is detected on port 17, regardless of whatever   
# else is happening in the program, the function my_callback will be run  
GPIO.add_event_detect(17, GPIO.RISING, callback=my_callback, bouncetime=300)  
  
  
try:  
    print "Waiting for rising edge on port 17"  
    GPIO.wait_for_edge(17, GPIO.RISING)  
    print "Rising edge detected on port 17. Here endeth the third lesson."  
  
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  
