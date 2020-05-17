import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setup(11, GPIO.IN)

while True:
  i=GPIO.input(11)
  
  if i==0:
    print("No intruders",i)
    time.sleep(0.1)
  elif i==1:
    print("Intruder detected",i)
  time.sleep(0.1)
