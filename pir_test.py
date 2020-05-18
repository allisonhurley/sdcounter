import time
import digitalio
import board
import busio

pir = digitalio.DigitalInOut(board.D17)
pir.direction = digitalio.Direction.INPUT
pir.pull = digitalio.Pull.UP
 

while True:
    
    if event.edge == pir.EDGE_FALLING:
        print("intruder detected")
        time.sleep(0.1)
        
    elif event.edge == pir.EDGE_RISING:
        print("NONE")
        time.sleep(0.1)
 
