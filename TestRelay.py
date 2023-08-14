import RPi.GPIO as GPIO
from time import sleep

relay = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)

try:
    while True:
        GPIO.output(relay, 1)
        print(f"Relay is OFF")
        sleep(5)
        GPIO.output(relay, 0)
        print(f"Relay is ON")
        sleep(5)

finally:
    GPIO.cleanup()   
    print("clean up")     