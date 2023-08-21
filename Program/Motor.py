import RPi.GPIO as GPIO
from time import sleep

class Step:
    def __init__(self, enaPin, dirPin, pulPin, ls1, ls2):
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(enaPin, GPIO.OUT)
        GPIO.setup(dirPin, GPIO.OUT)
        GPIO.setup(pulPin, GPIO.OUT)
        GPIO.setup(ls1, GPIO.IN)
        GPIO.setup(ls2, GPIO.IN)
 
        self.enable = enaPin
        self.direction = dirPin
        self.pulsa = pulPin
        self.kanan = ls1
        self.kiri = ls2

        self.counterCW = 0
        self.counterCCW = 0
    
    def boleh(self):
        GPIO.output(self.enable, 0)
        
    def stop(self):
        GPIO.output(self.enable, 1)
        
    def signal(self):
        self.boleh() 
        for x in range(75):     
            GPIO.output(self.pulsa, 1)
            sleep(0.00025)
            GPIO.output(self.pulsa, 0)
            sleep(0.00025)                         
        
    def cW(self):
        GPIO.output(self.direction, True)
        
    def ccW(self):
        GPIO.output(self.direction, False)

    def limitL(self):
        tombol = GPIO.input(self.kiri)
        state = 0
        if tombol == 0 and state == 0:
            state = 1
            self.counterCW += 1
            sleep(0.5)
        elif tombol == 0 and state == 1:
            print("pressed")
        return tombol        
    
    def limitR(self):
        tombol = GPIO.input(self.kanan)
        state = 0
        if tombol == 0 and state == 0:
            state = 1
            self.counterCCW += 1 
            sleep(1.5)
        elif tombol == 0 and state == 1:
            print("pressed")  
        return tombol 

    def go(self):
        self.signal()
        limitL = self.limitL()
        limitR = self.limitR()
        if limitL == 1 and limitR == 1:
            self.signal()
        elif limitL == 0:
            print("Putar ke Arah Jarum Jam")
            print(f"Putaran Searah: {self.counterCW}\n")
            self.cW()
        elif limitR == 0:
            print("Putar ke Berlawanan Jarum Jam")
            print(f"Putaran Berlawanan: {self.counterCCW}\n")
            self.ccW()
        elif limitL == 0 and limitR == 0:
            self.stop()   
        while self.counterCCW >= 7:
            self.stop() 
            print("Done")  

        



