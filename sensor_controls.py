import time
import busio
import digitalio
import board
import adafruit_amg88xx

from datetime import datetime # for testing purposes

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

pir = digitalio.DigitalInOut(board.D17)
pir.direction = digitalio.Direction.INPUT
pir.pull = digitalio.Pull.UP

people_in_store = 0
temp_count = 0

while True:     #if PIR sensor detects movement first, the person is entering. If cam detects person first, the person is leaving
    
    new_list = sum(amg.pixels, [])
    count = sum(map(lambda x : x> 23, new_list))

    while count > 0: #while the camera detects a person's temperatures
        new_list = sum(amg.pixels, []) #convert 2D array to list so we don't have to iterate
        count = sum(map(lambda x: x>23, new_list)) #get number of temps in list greater than 23 degrees
        if ((count >= 2) and (count_flag == 0)):
            cameraTime = datetime.now()
            person_detected = 1 #detected person in front of camera flag set 
            count_flag = 1 #set count flag so people not counted more than once
                    
    if (pir.value == True and person_detected == 1):
        if people_in_store > 0:
            people_in_store = people_in_store - 1 ## if it's not the last person in the store, subtract from count of people in store
        
    count_flag = 0 #reset flags 
    person_detected = 0
    
    time.sleep(0.3) #small time delay
       
    if pir.value == True:               #When output from motion sensor is HIGH first NOT SURE IF IT SHOULD BE A WHILE OR IF???
        new_list = sum(amg.pixels, [])
        count = sum(map(lambda x : x> 23, new_list))
        
        while count > 0: #while the camera detects a person's temperatures
            new_list = sum(amg.pixels, []) #convert 2D array to list so we don't have to iterate
            count = sum(map(lambda x: x>23, new_list)) #get number of temps in list greater than 23 degrees
            
            if ((count >= 2) and (count_flag == 0)):
                people_in_store = people_in_store + 1 
                count_flag = 1 #set count flag so people not counted more than once
       break # break out of pir loop             
                
    count_flag = 0 #reset flags
    person_detected = 0 
    print("There are ", people_in_store, " people in the store.")
    print("")
    print("\n")
    
