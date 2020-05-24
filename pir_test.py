import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(PIR_PIN, GPIO.RISING)

while True:
    if GPIO.event_detected(PIR_PIN): 
        print("Motion detected")    
        
    time.sleep(1)
