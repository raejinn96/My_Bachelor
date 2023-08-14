import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(5, GPIO.OUT)

pinA = 23 # kiri
pinB = 24 # kanan
relay = 5
# def limitL(pin):
#     diPencet = 0
#     hitung = 0
#     pencetState = GPIO.input(pin)
#     if (pencetState == 0) and diPencet == 0:
#         diPencet = 1
#         hitung += 1
#         # pencetState = GPIO.input(pin)
#     elif (pencetState == 0) and diPencet == 1:
#         print("Pressed")
#         # pencetState = GPIO.input(pin)
#     else:
#         diPencet = 0   
#     print(f"\nBanyak: {hitung}")
#     return pencetState       

try:
    while True:
        if GPIO.input(pinA) == 1:
            # GPIO.output(relay, 1)
            print("idle_Kiri")
        else:
            # GPIO.output(relay, 1)
            print("Kiri")
            

        if GPIO.input(pinB) == 1:
            # GPIO.output(relay, 1)
            print("idle_Kanan")
        else:
            # GPIO.output(relay, 1)
            print("Kanan")
            

        if GPIO.input(pinA) == 0 and GPIO.input(pinB) == 0:
            GPIO.output(relay, 0)
            print("active")
        else:
            GPIO.output(relay, 1) 

        sleep(0.2)          

except KeyboardInterrupt:
    print("Interrupted")
    
finally:
    GPIO.cleanup()         
    print("Clear")   

