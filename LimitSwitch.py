import RPi.GPIO as GPIO
from time import sleep

class Limit():
    def __init__(self, ls1, ls2):
        self.kiri = ls1
        self.kanan = ls2

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(ls1, GPIO.IN)
        GPIO.setup(ls2, GPIO.IN)

    def limitL(self):
        kiri = GPIO.input(self.kiri)
        sleep(0.001)
        return kiri
  
    
    def limitR(self):
        kanan = GPIO.input(self.kanan)
        sleep(0.001)
        return kanan
      
