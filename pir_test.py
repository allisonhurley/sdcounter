import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
    if GPIO.input(17):     # if port 17 == 1  
        rising_time = datetime.now()
        print("Rising edge detected on 17 ",rising_time)  
    else:                  # if port 17 != 1  
        falling_time = datetime.now()
        print("Falling edge detected on 17 ", falling_time) 
try:
    GPIO.add_event_detect(PIR_PIN, GPIO.BOTH, callback=MOTION)
    while 1:
        time.sleep(100)
        
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
