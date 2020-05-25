import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
PIR_PIN1 = 17
PIR_PIN2 = 27
GPIO.setup(PIR_PIN1, GPIO.IN)
GPIO.setup(PIR_PIN2, GPIO.IN)

def MOTION1(PIR_PIN1):
    if GPIO.input(17):     # if port 17 == 1  
        pir1_rising = datetime.now()
        pir2_flag = 1
        print("Rising edge detected on 17 ",pir1_rising)  
    else:                  # if port 17 != 1  
        pir1_falling = datetime.now()
        print("Falling edge detected on 17 ", pir1_falling)
        
def MOTION2(PIR_PIN2):
    if GPIO.input(27):     # if port 17 == 1  
        pir2_rising = datetime.now()
        pir2_flag = 1
        print("Rising edge detected on 27 ",pir2_rising)  
    else:                  # if port 17 != 1  
        pir2_falling = datetime.now()
        print("Falling edge detected on 27 ", pir2_falling) 

#set flags
pir1_flag = 0
pir2_flag = 0

try:
    GPIO.add_event_detect(PIR_PIN1, GPIO.BOTH, callback=MOTION1)
    GPIO.add_event_detect(PIR_PIN2, GPIO.BOTH, callback=MOTION2)
    while 1:
        if (pir1_flag == 1) and (pir2_flag == 0):
            people_in_store += 1
        elif (pir1_flag == 0) and (pir2_flag == 1):
            if people_in_store > 0:
                people_in_store -= 1
        
        #reset flags
        pir1_flag = 0
        pir2_flag = 0
    print("There are ", people_in_store, "people in the store")
    print("")
    print("\n")
    
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup() 
