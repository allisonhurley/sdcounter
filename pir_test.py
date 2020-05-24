import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
pir1 = 17
pir2 = 27
GPIO.setup(pir1, GPIO.IN)
GPIO.setup(pir2, GPIO.IN)

def PIR1MOTION(pir1):  
    pir1_time = datetime.now()
    pir1_flag = 1
    
def PIR2MOTION(pir2):
    pir2_time = datetime.now()
    pir2_flag = 1

GPIO.add_event_detect(pir1, GPIO.RISING, callback=PIR1MOTION)
GPIO.add_event_detect(pir2, GPIO.RISING, callback=PIR2MOTION)

#initialize time values to be equal
pir1_time = datetime.now()
pir2_time = pir1_time
people_in_store = 10
pir1_flag = 0
pir2_flag = 0

while True:
    if (pir1_flag == 1) and (pir2_flag == 1):
        if pir1_time > pir2_time:
            if people_in_store > 0:
                people_in_store -= 1
        elif pir1_time < pir2_time:
            people_in_store += 1
        else:
            people_in_store = people_in_store

        pir1_time = pir_2_time #reset flags to be equal until next rising edge
        pir1_flag = 0
        pir2_flag = 0
    
    print("There are ", people_in_store, "in the store")
    print("")
    print("\n")
