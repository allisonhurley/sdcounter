import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)


def MOTION(PIR_PIN):
    if GPIO.input(17):     # if port 17 == 1  
        PIR_rising = datetime.now()
        print("Rising edge detected on 17 ",PIR_rising)  
    else:                  # if port 17 != 1  
        PIR_falling = datetime.now()
        print("Falling edge detected on 17 ",PIR_falling) 

GPIO.add_event_detect(PIR_PIN, GPIO.BOTH, callback=MOTION)
motion_detected = 0


while True:
    
    time.sleep(.1)
