import time
from datetime import datetime
import numpy as np
import busio
import digitalio
import board
import adafruit_amg88xx
import RPi.GPIO as GPIO

pir1 = 17
pir2 = 27
GPIO.setup(pir1, GPIO.IN)
GPIO.setup(pir2, GPIO.IN)
    
GPIO.add_event_detect(pir1, GPIO.RISING)
GPIO.add_event_detect(pir2, GPIO.RISING)

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)
        
people_in_store = 0 #initialize flags to 0
prev_people = 0
count = 0
count_flag = 0 
pir1_flag = 0
pir2_flag = 0       

while True:     #if PIR sensor detects movement first, the person is entering. If cam detects person first, the person is leaving 
      
    new_list = sum(amg.pixels, [])   #converts 2D array to list and counts number of temps > 23 in list
    count = sum(map(lambda x : x> 23, new_list))

        #wait for person to step out of camera detection area before comparing time stamps
    while count > 0: #while the camera detects a person's temperatures

        if ((count > 0) and (count_flag == 0)): # if any number of temps > 23 FOR NOW COME BACK AND FIX?
            camera_time = datetime.now()
            print("camera time ", camera_time)
            count_flag = 1 #set count flag so people not counted more than once
        
        new_list = sum(amg.pixels, []) #convert 2D array to list so we don't have to iterate
        count = sum(map(lambda x: x>23, new_list)) #get number of temps in list greater than 23 degrees
   
    while(pir1_flag == 0 and pir2_flag == 0):
        if ((GPIO.event_detected(pir1) and count_flag == 1) and (pir1_flag == 0)):
            pir1_time = datetime.now()
            pir1_flag = 1
            count_flag = 0
            if (people_in_store > 0):
                people_in_store -= 1
        elif ((GPIO.event_detected(pir2) and count_flag == 1) and (pir2_flag == 0)):
            pir2_time = datetime.now()
            pir2_flag = 1   
            count_flag = 0
            people_in_store += 1


    
    if people_in_store != prev_people: #if number of people in store has changed, output values
       if pir1_flag == 1:
           print("pir1 time ", pir1_time) 
       if pir2_flag == 1:
           print("pir2 time ", pir2_time) 
       print("There are ", people_in_store, " people in the store.")
       print("")
       print("\n")
       prev_people = people_in_store
    #reset flags
    count_flag = 0
    pir1_flag = 0
    pir2_flag = 0 
        
    

   
