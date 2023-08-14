import RPi.GPIO as GPIO
from time import sleep

sigPin = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(sigPin, GPIO.OUT)
GPIO.output(sigPin, 1)

try:
    while True:
        print("Satu")
        GPIO.output(sigPin, 1)
        sleep(2)
        GPIO.output(sigPin, 0)
        sleep(4)

        print("Dua")
        GPIO.output(sigPin, 1)
        sleep(2)
        GPIO.output(sigPin, 0)
        sleep(4)

        print("Tiga")
        GPIO.output(sigPin, 1)
        sleep(2)
        GPIO.output(sigPin, 0)
        sleep(4)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Interrupted")
    
finally :
    GPIO.cleanup()
    print("Clear")




# class Pompa:
#     def __init__(self, sigPin):

#         GPIO.setmode(GPIO.BCM)
#         GPIO.setup(sigPin, GPIO.OUT)

#         self.sinyal = sigPin

#         GPIO.output(self.sinyal, 1)
    
#     def nyala(self):
#         GPIO.output(self.sinyal, 0)

#     def mati(self):
#         GPIO.output(self.sinyal, 1)    