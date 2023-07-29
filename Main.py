import RPi.GPIO as GPIO
from time import sleep
from Motor import Step
from CountTo1 import Count

limit1 = 23
limit2 = 24
en = 17
dir = 27
pul = 22

try:
    Count.hitungMundur()
    step = Step(en, dir, pul, limit1, limit2)           # Membuat objek dari class Step

    while True:
        step.go()
        print(f"Putaran Searah: {step.counterCW}\n")
        print(f"Putaran Anti: {step.counterCCW}\n")
        
except KeyboardInterrupt:     
    print("\nIntrupsi") 

finally:
    GPIO.cleanup()
    print("clear")


