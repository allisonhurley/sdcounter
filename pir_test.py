import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
PIR_PIN1 = 17
PIR_PIN2 = 27
GPIO.setup(PIR_PIN1, GPIO.IN)
GPIO.setup(PIR_PIN2, GPIO.IN)

#set flags
people_in_store = 10
prev_people = 10

GPIO.add_event_detect(PIR_PIN1, GPIO.RISING)
GPIO.add_event_detect(PIR_PIN2, GPIO.RISING)

while True:
    
    if (GPIO.event_detected(PIR_PIN1)):
        print("PIR 1 MOTION DETECTED")
        print("")
        print("\n")

    if (GPIO.event_detected(PIR_PIN2)):
        print("PIR 2 MOTION DETECTED")
        print("")
        print("\n")
