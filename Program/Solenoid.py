import RPi.GPIO as GPIO
from time import sleep


class Solenoid:
    def __init__(self, sigPin):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sigPin, GPIO.OUT)

        self.sinyal = sigPin

        GPIO.output(self.sinyal, 1)
    
    def nyala(self):
        GPIO.output(self.sinyal, 0)
    
    def mati(self):
        GPIO.output(self.sinyal, 1)    