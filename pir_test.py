import digitalio
import time
import board


pir = digitalio.DigitalInOut(board.D17)
pir.direction = digitalio.Direction.INPUT
pir.pull = digitalio.Pull.UP

 
while True:
    prev_pir_val = pir.value
    time.sleep(0.4) #small time delay of 200 ms
    if pir.value == False and prev_pir_val == True: #When output from motion sensor is HIGH

        print ("Intruder detected",pir.value)

        time.sleep(0.1)
        
    else: #When output from motion sensor is LOW

        print ("try again")

        time.sleep(0.1)
