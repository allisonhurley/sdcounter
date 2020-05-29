#this file is to test how the camera counts people

import time
import busio
import board
import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

count = 0
people_in_store = 0
prev_people = 0
count_flag = 0


while True:   

    new_list = sum(amg.pixels, [])
    count = sum(map(lambda x : x> 23, new_list))

    while count > 0:
        new_list = sum(amg.pixels, [])
        count = sum(map(lambda x: x>23, new_list))
        if ((count >= 2) and (count_flag == 0)):
            people_in_store = people_in_store + 1
            count_flag = 1 #set count flag so people not counted more than once
            prev_people = people_in_store

    if people_in_store != prev_people:
        for row in amg.pixels:
        # Pad to 1 decimal place
            print(["{0:.1f}".format(temp) for temp in row])
            print("")
        print("\n")

        print("There are {people_in_store} people in the store.")
        print("")
        print("\n")
    
    count_flag = 0 #reset flag
