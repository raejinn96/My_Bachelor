
import sys
import RPi.GPIO as gpio 
import time

try: 
    direction = "left"
    steps1 = 800
    steps2 = 1200
except:
    steps = 0
 
gpio.setmode(gpio.BCM)
#GPIO23 = Direction
#GPIO24 = Step
#GPIO25 = Enable
gpio.setup(27, gpio.OUT) 
gpio.setup(22, gpio.OUT)
gpio.setup(17, gpio.OUT)

StepCounter = 0
waktu = 0
 
while StepCounter < steps1:
 
    #turning the gpio on and off tells the easy driver to take one step
    gpio.output(22, True)
    time.sleep(0.0025)
    gpio.output(22, False)
    time.sleep(0.0025)
    gpio.output(27, False)
    waktu += 0.0059
    StepCounter += 1
    print("Level 1: ")
    print(StepCounter)
    print(f"{round(waktu, 2)} detik\n")
    
    
while StepCounter < steps2:
 
    #turning the gpio on and off tells the easy driver to take one step
    gpio.output(22, True)
    time.sleep(0.0025)
    gpio.output(22, False)
    gpio.output(27, True)
    waktu += 0.0059
    time.sleep(0.0025)
    StepCounter += 1
    print("Level 2: ")
    print(StepCounter)
    print(f"{round(waktu, 2)} detik\n")

