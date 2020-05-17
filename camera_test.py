#this file is to test how the camera counts people

import time
import busio

import board
import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

temp_count = 0
people_in_store = 0

while True:     #if PIR sensor detects movement first, the person is entering. If cam detects person first, the person is leaving
    
    for row in amg.pixels: #check to see if camera detects person
        for j in row:           #look through temps in a row
            if j > 22.0:        #detect a human temp (usually > 22 degrees celsius)
                temp_count = temp_count + 1
                time.sleep(.1) #time delay
                
            if temp_count >= 2:
                people_in_store = people_in_store + 1
                temp_count = 0 #reset temp count
                break
            break
    
    print("There are ", people_in_store, " people in the store B.")
    print("")
    print("\n")
