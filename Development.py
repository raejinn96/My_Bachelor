import RPi.GPIO as GPIO
from time import sleep

class Step:
    def __init__(self, enaPin, dirPin, pulPin, ls1, ls2):
        
        self.enable = enaPin
        self.direction = dirPin
        self.pulsa = pulPin
        self.kiri = ls1
        self.kanan = ls2

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(enaPin, GPIO.OUT)
        GPIO.setup(dirPin, GPIO.OUT)
        GPIO.setup(pulPin, GPIO.OUT)
        GPIO.setup(ls1, GPIO.IN)
        GPIO.setup(ls2, GPIO.IN)
    
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

    def limitL(self):
        kiri = GPIO.input(self.kiri)
        sleep(0.001)
        return kiri
  
    def limitR(self):
        kanan = GPIO.input(self.kanan)
        sleep(0.001)
        return kanan    

    def go(self):
        if self.limitL() == 1 and self.limitR() == 1:
            self.signal()
        elif self.limitL() == 0:
            self.cW()
        elif self.limitR() == 0:
            self.ccW()
        elif self.limitL() == 0 and self.limitR() == 0:
            self.stop()   
           

        



