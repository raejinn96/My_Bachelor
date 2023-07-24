import RPi.GPIO as GPIO
from time import sleep
from StepperMotor import Stepper
from LimitSwitch import Limit

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
        step = Stepper(en, dir, pul)
        ls = Limit(limit1, limit2)
    
        ls_kiri = ls.limitL()
        ls_kanan = ls.limitR()

        if ls_kiri == 1 and ls_kanan == 1:
            step.signal()
        elif ls_kiri == 0:
            step.cW()
        elif ls_kanan == 0:
            step.ccW()
        elif ls_kanan == 0 and ls_kiri == 0:
            step.stop()   
        
except KeyboardInterrupt:     
    print("\nIntrupsi") 

finally:
    GPIO.cleanup()
    print("clear")


