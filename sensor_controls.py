import time
import busio
import board
import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor

while True:     #if PIR sensor detects movement first, the person is entering. If cam detects person first, the person is leaving
    i=GPIO.input(11)
    if i==0:                 #When output from motion sensor is LOW
        print("No intruders",i)
        for row in amg.pixels: #check to see if camera detects person
            for j in row:           #look through temps in a row
                if j > 22.0:        #detect a human temp (usually > 22 degrees celsius)
                   person_detected = 1
                   time.sleep(.25)
                   print("person leaving",j)
                   break
            break
        break

    elif i==1:               #When output from motion sensor is HIGH
        print("Intruder alert",i)
        motion_detected = 1
        time.sleep(.25)     #give 1/2 delay for person to enter building

        for row in amg.pixels: #check to see if camera detects person
            for j in row:           #look through temps in a row
                if j > 22.0:        #detect a human temp (usually > 22 degrees celsius)
                    person_detected = 1
                    print("Person entering",j)
                    break
            break
        break
        
            
    
    print("")
    print("\n")
    time.sleep(1) # 1 second delay I think?
