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

while True:
  
    if pir.value: #When output from motion sensor is HIGH

        print ("Intruder detected",pir.value)

        time.sleep(0.1)
        
    else: #When output from motion sensor is LOW

        print ("No intruders",pir.value)

        time.sleep(0.1)

people_in_store = 0;

while True:     #if PIR sensor detects movement first, the person is entering. If cam detects person first, the person is leaving
    
    if pir.value == False: #When output from motion sensor is LOW
                       
        for row in amg.pixels: #check to see if camera detects person
            for j in row:           #look through temps in a row
                if j > 22.0:        #detect a human temp (usually > 22 degrees celsius)
                                  
                   time.sleep(.25) #time delay of quarter of a second
                   if pir.value == True:
                        if people_in_store > 0:
                            people_in_store = people_in_store - 1 ## if it's not the last person in the store, subtract from count of people in store
               
            break
        break

    elif pir.value == True:               #When output from motion sensor is HIGH

        time.sleep(.25)     #give 1/4s delay for person to enter building

        for row in amg.pixels: #check to see if camera detects person
            for j in row:           #look through temps in a row
                if j > 22.0:        #detect a human temp (usually > 22 degrees celsius)
                    people_in_store = people_in_store + 1 #add to count of people in store
                    
            break
        break
    
    print("There are ", people_in_store, " people in the store.")
    print("")
    print("\n")
    time.sleep(2) # 2 second delay 
