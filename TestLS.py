import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

pinA = 23
pinB = 24

def limitL(pin):
    diPencet = 0
    hitung = 0
    pencetState = GPIO.input(pin)
    if (pencetState == 0) and diPencet == 0:
        diPencet = 1
        hitung += 1
        # pencetState = GPIO.input(pin)
    elif (pencetState == 0) and diPencet == 1:
        print("Pressed")
        # pencetState = GPIO.input(pin)
    else:
        diPencet = 0   
    print(f"\nBanyak: {hitung}")
    return pencetState       

try:
    while True:
        limitL(pinA)

except KeyboardInterrupt:
    print("Interrupted")
    
finally:
    GPIO.cleanup()         
    print("Clear")   

