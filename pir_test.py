import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)

GPIO.add_event_detect(PIR_PIN, GPIO.RISING)
motion_detected = 0

while True:
    
    try:
        if GPIO.event_detected(PIR_PIN):
            motion_detected += 1 
            print("Motion detected: ",motion_detected)
    finally:
        GPIO.cleanup()
        
    time.sleep(1)
