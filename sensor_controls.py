import time
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

GPIO.add_event_detect(PIR_PIN, GPIO.RISING) #we want to detect rising edge of PIR sensor

while True:     #if PIR sensor detects movement first, the person is entering. If cam detects person first, the person is leaving


    new_list = sum(amg.pixels, [])   #converts 2D array to list and counts number of temps > 23 in list
    count = sum(map(lambda x : x> 23, new_list))

    while count > 0: #while the camera detects a person's temperatures
        new_list = sum(amg.pixels, []) #convert 2D array to list so we don't have to iterate
        count = sum(map(lambda x: x>23, new_list)) #get number of temps in list greater than 23 degrees
        
        if ((count >= 2) and (count_flag == 0)):
            person_detected = 1 #detected person in front of camera flag set 
            count_flag = 1 #set count flag so people not counted more than once
        
        if (GPIO.event_detected(PIR_PIN) and person_detected==1):                
            if people_in_store > 0:
                people_in_store = people_in_store - 1 ## if it's not the last person in the store, subtract from count of people in store

    count_flag = 0 #reset flags 
    person_detected = 0


    time.sleep(0.3) #small time delay

    if GPIO.event_detected(PIR_PIN):          #When output from motion sensor is HIGH first NOT SURE IF IT SHOULD BE A WHILE OR IF???
        new_list = sum(amg.pixels, [])
        count = sum(map(lambda x : x> 23, new_list))

        while count > 0: #while the camera detects a person's temperatures
            new_list = sum(amg.pixels, []) #convert 2D array to list so we don't have to iterate
            count = sum(map(lambda x: x>23, new_list)) #get number of temps in list greater than 23 degrees

        if ((count >= 2) and (count_flag == 0)):
            people_in_store = people_in_store + 1 
            count_flag = 1 #set count flag so people not counted more than onc


    count_flag = 0 #reset flags
    person_detected = 0 

    print("There are ", people_in_store, " people in the store.")
    print("")
    print("\n")
    time.sleep(0.3) #small time delay    
