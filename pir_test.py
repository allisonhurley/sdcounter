#!/usr/bin/env python2.7  
# script by Alex Eames https://raspi.tv  
# https://raspi.tv/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3  
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
  
# GPIO 23 & 17 set up as inputs, pulled up to avoid false detection.  
# Both ports are wired to connect to GND on button press.  
# So we'll be setting up falling edge detection for both  

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  

  
# now we'll define two threaded callback functions  
# these will run in another thread when our events are detected  
def my_callback(channel):  
    print ("falling edge detected on 17")  
    
While True:
  
# when a falling edge is detected on port 17, regardless of whatever   
# else is happening in the program, the function my_callback will be run  
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, bouncetime=300)  



