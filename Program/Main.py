import RPi.GPIO as GPIO
from time import sleep

from Motor import Step
# from Pompa import Pompa 
from Rain import Hujan
from CountTo1 import Count

limit1 = 23
limit2 = 24
en = 17
dir = 27
pul = 22
rainPin = 26
sole = 5

step = Step(en, dir, pul, limit1, limit2)  # Membuat objek dari class Step
hujan = Hujan(rainPin)

# sole = Pompa(sole)

try:
    # step.stop()
    # sleep(3)
    # Count.hitungMundur()
    # step = Step(en, dir, pul, limit1, limit2)          

    while True:
        
        hujan.cek()
        # step.go()
        # while step.counterCW < 4:
        #     sole.nyala()
    
        
        
        
except KeyboardInterrupt:     
    print("\nIntrupsi") 

finally:
    GPIO.cleanup()
    print("clear")


