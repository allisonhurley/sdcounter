import time
import busio
import digitalio
import board
import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

pir = digitalio.DigitalInOut(board.D17)
pir.direction = digitalio.Direction.INPUT
pir.pull = digitalio.Pull.UP

people_in_store = 0
temp_count = 0

while True:     #if PIR sensor detects movement first, the person is entering. If cam detects person first, the person is leaving

    for row in amg.pixels: #check to see if camera detects person
        for j in row:           #look through temps in a row
            if j > 22.0:        #detect a human temp (usually > 22 degrees celsius)
                temp_count = temp_count + 1
                time.sleep(.1) #time delay 
                
                if pir.value == True && temp_count >= 2:
                    if people_in_store > 0:
                        people_in_store = people_in_store - 1 ## if it's not the last person in the store, subtract from count of people in store
                print("There are ", people_in_store, " people in the store A.")
            break
        #break

   if pir.value == True:               #When output from motion sensor is HIGH

        time.sleep(.1)     #time delay

        for row in amg.pixels: #check to see if camera detects person
            for j in row:           #look through temps in a row
                if j > 22.0:        #detect a human temp (usually > 22 degrees celsius)
                    temp_count = temp_count + 1
                    time.sleep(.1) #time delay 
                    
                    if temp_count >= 2:
                        print("There are ", people_in_store, " people in the store B.")
                break
        #break

    print("There are ", people_in_store, " people in the store C.")
    print("")
    print("\n")
    time.sleep(.5) # 1/2 second delay 
