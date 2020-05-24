import time
from datetime import datetime
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

def MOTION(PIR_PIN):
    if GPIO.input(17):     # if port 17 == 1  
        PIR_rising = datetime.now()
        print("Rising edge detected on 17 ",rising_time)  
    else:                  # if port 17 != 1  
        PIR_falling = datetime.now()
        print("Falling edge detected on 17 ", falling_time) 
        
GPIO.add_event_detect(PIR_PIN, GPIO.BOTH, callback=MOTION)

while True:     #if PIR sensor detects movement first, the person is entering. If cam detects person first, the person is leaving

    try:

        new_list = sum(amg.pixels, [])   #converts 2D array to list and counts number of temps > 23 in list
        count = sum(map(lambda x : x> 23, new_list))

        while count > 0: #while the camera detects a person's temperatures
            new_list = sum(amg.pixels, []) #convert 2D array to list so we don't have to iterate
            count = sum(map(lambda x: x>23, new_list)) #get number of temps in list greater than 23 degrees

            if ((count > 0) and (count_flag == 0)): # if any number of temps > 23 FOR NOW COME BACK AND FIX?
                camera_time = datetime.now()
                print("camera time ", camera_time)
                count_flag = 1 #set count flag so people not counted more than once

            if camera_time > PIR_rising:
                people_in_store += 1
            elif (camera_time < PIR_rising) and (people_in_store > 0):
                people_in_store -= 1

    except:
        count = 0
        GPIO.cleanup()

    print("There are ", people_in_store, " people in the store.")
    print("")
    print("\n")
    count_flag = 0
    time.sleep(1) #time delay    
