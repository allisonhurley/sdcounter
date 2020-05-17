import time
import busio
import board
import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor

people_in_store = 0;

while True:     #if PIR sensor detects movement first, the person is entering. If cam detects person first, the person is leaving
    i=GPIO.input(11)
    if i==0:                 #When output from motion sensor is LOW
        
        for row in amg.pixels: #check to see if camera detects person
            for j in row:           #look through temps in a row
                if j > 22.0:        #detect a human temp (usually > 22 degrees celsius)
                                  
                   time.sleep(.25) #time delay of quarter of a second
                   i=GPIO.input(11) #check to see if PIR sensor detects person leaving
                   if i == 1:
                        if people_in_store > 0:
                            people_in_store -- ## if it's not the last person in the store, subtract from count of people in store
               
            break
        break

    elif i==1:               #When output from motion sensor is HIGH

        time.sleep(.25)     #give 1/4s delay for person to enter building

        for row in amg.pixels: #check to see if camera detects person
            for j in row:           #look through temps in a row
                if j > 22.0:        #detect a human temp (usually > 22 degrees celsius)
                    people_in_store ++ #add to count of people in store
                    
            break
        break
    
    print("There are ", people_in_store, " people in the store.")
    print("")
    print("\n")
    time.sleep(1) # 1 second delay I think?
