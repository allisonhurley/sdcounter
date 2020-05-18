import digitalio
import time
import board


pir = digitalio.DigitalInOut(board.D17)
pir.direction = digitalio.Direction.INPUT
pir.pull = digitalio.Pull.UP

 
while True:
    prev_pir_val = pir.value
  
    if pir.value == True and prev_pir_val == False: #When output from motion sensor is HIGH

        print ("Intruder detected",pir.value)

        time.sleep(0.1)
        
    else: #When output from motion sensor is LOW

        

        time.sleep(0.1)
