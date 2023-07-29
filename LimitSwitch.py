import RPi.GPIO as GPIO
from time import sleep

class Limit():
    def __init__(self, ls1, ls2):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(ls1, GPIO.IN)
        GPIO.setup(ls2, GPIO.IN)

        self.kiri = ls1
        self.kanan = ls2

    def limitL(self):
        diPencet = 0
        hitung = 0
        pencetState = GPIO.input(self.kiri)
        if (pencetState == 0) and diPencet == 0:
            hitung += 1
            diPencet = 1
            sekarang = GPIO.input(self.kiri)
        elif (pencetState == 0) and diPencet > 0:
        # while GPIO.input(self.kiri) == awal:
        #     sleep(0.001)
        # sleep(0.001)
        sekarang = GPIO.input(self.kiri)
        return sekarang
  
    def limitR(self):
        # awal= GPIO.input(self.kanan)
        # while GPIO.input(self.kanan) == awal:
        #     sleep(0.001)
        # sleep(0.001)
        sekarang = GPIO.input(self.kanan)
        return sekarang    