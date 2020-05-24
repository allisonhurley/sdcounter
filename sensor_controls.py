import time
from datetime import datetime
import numpy as np
import busio
import digitalio
import board
import adafruit_amg88xx
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)
        
people_in_store = 0 #initialize flags to 0
count = 0
count_flag = 0 
test_flag1 = 0
test_flag2 = 0
        
GPIO.add_event_detect(PIR_PIN, GPIO.BOTH)

while True:     #if PIR sensor detects movement first, the person is entering. If cam detects person first, the person is leaving

  
    #CASE 1: PIR SENSOR FIRST THEN CAMERA DETECTION
    if GPIO.event_detected(PIR_PIN):
        if GPIO.input(17):     # if port 17 == 1  
            pir_rising = datetime.now()
            test_flag1 = 1
            print("Rising edge detected on 17 ",PIR_rising)  
        else:                  # if port 17 != 1  
            pir_falling = datetime.now()
            print("Falling edge detected on 17 ",PIR_falling) 
      
    new_list = sum(amg.pixels, [])   #converts 2D array to list and counts number of temps > 23 in list
    count = sum(map(lambda x : x> 23, new_list))

        #wait for person to step out of camera detection area before comparing time stamps
    while count > 0: #while the camera detects a person's temperatures

        if ((count > 0) and (count_flag == 0)): # if any number of temps > 23 FOR NOW COME BACK AND FIX?
            camera_time = datetime.now()
            test_flag2 = 1
            print("camera time ", camera_time)
            count_flag = 1 #set count flag so people not counted more than once

        new_list = sum(amg.pixels, []) #convert 2D array to list so we don't have to iterate
        count = sum(map(lambda x: x>23, new_list)) #get number of temps in list greater than 23 degrees

    if ((test_flag1 == 1) and (test_flag2 == 1))
        if camera_time > PIR_rising:
            people_in_store += 1
        elif (camera_time < PIR_rising) and (people_in_store > 0):
            people_in_store -= 1
        
    #reset flags
    count_flag = 0
    person_detected = 0
    test_flag1 = 0
    test_flag2 = 0
        
    
    print("There are ", people_in_store, " people in the store.")
    print("")
    print("\n")
    time.sleep(1) #time delay    
