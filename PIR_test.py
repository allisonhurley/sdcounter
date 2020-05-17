import digitalio
import time
import board


pir = digitalio.DigitalInOut(board.D11)
pir.direction = digitalio.Direction.INPUT
pir.pull = digitalio.Pull.UP

 
while True:
  
    if pir.value: #When output from motion sensor is HIGH

        print ("Intruder detected",pir.value)

        time.sleep(0.1)
        
    else: #When output from motion sensor is LOW

        print ("No intruders",pir.value)

        time.sleep(0.1)

