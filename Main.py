import RPi.GPIO as GPIO
from time import sleep
from Motor import Step

limit1 = 23
limit2 = 24
en = 17
dir = 27
pul = 22

try:
    waktu = 3
    while waktu > 0:
        print(waktu)
        waktu -= 1
        sleep(1)
    print("Mulai")

    while True:
        step = Step(en, dir, pul, limit1, limit2)
    
        step.go()
        
except KeyboardInterrupt:     
    print("\nIntrupsi") 

finally:
    GPIO.cleanup()
    print("clear")


