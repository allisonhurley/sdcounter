import digitalio
import time
import board

pir = digitalio.DigitalInOut(board.D11)
pir.direction = digitalio.Direction.INPUT
pir.pull = digitalio.Pull.UP

 
while True:
  
    if pir.value==0: #When output from motion sensor is LOW
  
        print ("No intruders",i)

        time.sleep(0.1)

    elif pir.value==1: #When output from motion sensor is HIGH

        print ("Intruder detected",i)

        time.sleep(0.1)
