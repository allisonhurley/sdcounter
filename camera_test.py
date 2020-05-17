#this file is to test how the camera counts people

import time
import busio

import board
import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

temp_count = 1
people_in_store = 0
count_flag = 0


while True:     #if PIR sensor detects movement first, the person is entering. If cam detects person first, the person is leaving
   
    while temp_count != 0: #break out of loop when temp_count = 0
        for row in amg.pixels: #check to see if camera detects person
            for j in row:           #look through temps in a row

            # count numbers in the list which are greater than 25
                temp_count = sum(map(lambda x : x>25, amg.pixels))

                if ((temp_count >= 2) and (count_flag == 0)):
                    people_in_store = people_in_store + 1
                    temp_count = 0 #reset temp count
                    count_flag = 1 #set count flag so people not counted more than once
                    break
               break
        
    for row in amg.pixels:
        # Pad to 1 decimal place
        print(["{0:.1f}".format(temp) for temp in row])
        print("")
    print("\n")
    
    
    
    print("There are ", people_in_store, " people in the store B.")
    print("")
    print("\n")
