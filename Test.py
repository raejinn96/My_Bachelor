import RPi.GPIO as GPIO
from time import sleep

limit1 = 23
limit2 = 24
en = 17
dir = 27
pul = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(limit1, GPIO.IN)
GPIO.setup(limit2, GPIO.IN)
GPIO.setup(en, GPIO.OUT)
GPIO.setup(dir, GPIO.OUT)
GPIO.setup(pul, GPIO.OUT)

def pulsa():
    GPIO.output(pul, 1)
    sleep(0.01)  
    GPIO.output(pul, 0)
    sleep(0.01)   

try:
    while True:
        GPIO.output(en, 0)
        print("\nMulai")

        if (GPIO.input(limit1) == 1) and (GPIO.input(limit2) == 1):
            pulsa()
            GPIO.output(dir, 1)
        elif GPIO.input(limit2) == 0:
            pulsa()
            GPIO.output(dir, 0)
        elif GPIO.input(limit1) == 0 and GPIO.input(limit2) == 0:
            GPIO.output(en, 1)

        
       
        # sleep(5)
        # sleep(5)
        # GPIO.output(en, 1)

except KeyboardInterrupt:     
    print("\nIntrupsi") 

finally:
    GPIO.cleanup()
    print("clear")        

