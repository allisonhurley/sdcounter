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
   
      for row in amg.pixels

      # count numbers in the row greater than 25
          count = sum(map(lambda x : x>25, row)) 
          temp_count = temp_count + count #count all numbers greater than 25 in whole array
            
          if ((temp_count >= 4) and (count_flag == 0)):
              people_in_store = people_in_store + 1
              count_flag = 1 #set count flag so people not counted more than once
                 
       time.sleep(1) # 1 s time delay until next scan
              
        
    for row in amg.pixels:
        # Pad to 1 decimal place
        print(["{0:.1f}".format(temp) for temp in row])
        print("")
    print("\n")
    
    
    count_flag = 0 #reset count flag

    print("There are ", people_in_store, " people in the store B.")
    print("")
    print("\n")
