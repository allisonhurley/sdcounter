import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
     print("Motion Detected")

print("PIR Module Test (CTRL+C to exit)")
time.sleep(2)
print("Ready")


