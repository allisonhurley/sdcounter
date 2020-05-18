#this file is to test how the camera counts people

import time
import busio
import numpy as np
import board
import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

count = 0
people_in_store = 0
count_flag = 0


while True:     #if PIR sensor detects movement first, the person is entering. If cam detects person first, the person is leaving
   
   new_list = sum(amg.pixels, [])
   count = sum(map(lambda x : x> 23, new_list))
   if len(new_list.shape) == 1:
      print('1-D array new_list')
   if len(new_list.shape) == 2:
      print('2-D array new_list')
   if len(amg.pixels.shape) == 1:
      print('1-D array')
   if len(amg.pixels.shape) == 2:
      print('2-D array')               
   print("")
   print("\n")               
   time.sleep(1)
   
   #while count > 0:
        #new_list = sum(amg.pixels, [])
        #count = sum(map(lambda x: x>23, new_list)
           # if ((count >= 2) and (count_flag == 0)):
             #   people_in_store = people_in_store + 1
               # count_flag = 1 #set count flag so people not counted more than once
     
   #for row in amg.pixels:
      # Pad to 1 decimal place
      #print(["{0:.1f}".format(temp) for temp in row])
      #print("")
   #print("\n")


   #count_flag = 0 #reset count flag
   #print("There are ", people_in_store, " people in the store B.")
   #print("")
   #print("\n")
