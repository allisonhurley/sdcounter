import time
import busio
import board
import adafruit_amg88xx
 
i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)


while True: 
    for row in amg.pixels:
        # Pad to 1 decimal place
        print(["{0:.1f}".format(temp) for temp in row])
        print("")
    print("\n")
 
    
    for row in amg.pixels:
        for i in row:
            if i > 22.0:
                person_detected = 1
                break
            else:
                person_detected = 0
            
    if person_detected == 1:
        print("Person detected",i)
    else:
        print("No one detected",i)

    print("")
    print("\n")
    time.sleep(1)
