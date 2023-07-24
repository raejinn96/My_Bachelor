import RPi.GPIO as GPIO
from time import sleep

class Stepper:
    def __init__(self, enaPin, dirPin, pulPin):
        
        self.enable = enaPin
        self.direction = dirPin
        self.pulsa = pulPin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(enaPin, GPIO.OUT)
        GPIO.setup(dirPin, GPIO.OUT)
        GPIO.setup(pulPin, GPIO.OUT)
    

    def boleh(self):
        GPIO.output(self.enable, 0)
        
    def stop(self):
        GPIO.output(self.enable, 1)
        
    def signal(self):
        self.boleh()
        GPIO.output(self.pulsa, 1)
        sleep(0.0025)
        GPIO.output(self.pulsa, 0)
        sleep(0.0025) 
    
    def cW(self):
        self.signal()  
        GPIO.output(self.direction, True)
        print("kanan") 
        
    def ccW(self):
        self.signal()   
        GPIO.output(self.direction, False)
        print("kiri") 


           

        



