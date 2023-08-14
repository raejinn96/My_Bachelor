import RPi.GPIO as GPIO
from time import sleep

class Hujan:
    def __init__(self, sigPin):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sigPin, GPIO.IN)
        
        self.sinyal = sigPin

    def cek(self):
        baca = GPIO.input(self.sinyal)   
        if baca == 0:
            print("Hujan")
            sleep(1)
        else:
            print("Normal")
            sleep(1)
        return baca         

