#Step 0: Preamble
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#Program Title  : easy_stepper.py 
#Code Written by: Salty Scott
#Current Project: www.rowboboat.com
#This code is a very basic example of using python to control a spark fun
# easy driver.  The spark fun easy driver that I am using in this example
# is connected to a 42HS4013A4 stepper motor and my raspberry pi.  Pin 23
# is the direction control and pin 24 is the step control.  I am using
# these components in the www.rowboboat.com project version 2.0 and I
# hope someone finds this a useful and simple example.
# This program expects two arguments: direction and steps
# Example usage: sudo python easy_stepper.py left 1600
# The above example would turn a 200 step motor one full revolution as by
# default the easy driver 4.4 is in 1/8 microstep mode. However the stepper driver 
# selected by gtaagii will default to one full step per step pulse, #microstepping can
# be selected if desired.
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
#Step 1: Import necessary libraries 
#------------------------------------------------------------------------
#------------------------------------------------------------------------
import sys
import RPi.GPIO as gpio #https://pypi.python.org/pypi/RPi.GPIO more info
import time
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
#Step 2: Read arguements https://www.youtube.com/watch?v=kQFKtI6gn9Y
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#read the direction and number of steps; if steps are 0 exit 
#using 16 microsteps per step 3200 for a full revoloution
try: 
    direction = "left"
    steps1 = 800
    steps2 = 1200
except:
    steps = 0
 
#print which direction and how many steps 
#print("You told me to turn %s %s steps.") % (direction, steps)
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
 
#Step 3: Setup the raspberry pi's GPIOs
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#use the broadcom layout for the gpio
gpio.setmode(gpio.BCM)
#GPIO23 = Direction
#GPIO24 = Step
#GPIO25 = Enable
gpio.setup(27, gpio.OUT) 
gpio.setup(22, gpio.OUT)
gpio.setup(17, gpio.OUT)
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
 
#Step 4: Set direction of rotation
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#set the output to true for left and false for right
# if direction == 'left':
#     gpio.output(27, False)
# elif direction == 'right':
#     gpio.output(27, True)

#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
 
#Step 5: Setup step counter and speed control variables
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#track the number of steps taken


#waittime controls speed
#------------------------------------------------------------------------
#------------------------------------------------------------------------
StepCounter = 0
waktu = 0
 
#Step 6: Let the magic happen
#------------------------------------------------------------------------
#------------------------------------------------------------------------
# Start main loop
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

    
# while StepCounter < steps3:
 
#     #turning the gpio on and off tells the easy driver to take one step
#     gpio.output(22, True)
#     time.sleep(0.0015)
#     gpio.output(22, False)
#     StepCounter += 1
#     WaitTimeDecel += 0.0005
#     print(StepCounter)
 
#     #Wait before taking the next step...this controls rotation speed
#     time.sleep(WaitTimeDecel)
#     gpio.cleanup()
# #------------------------------------------------------------------------
# #------------------------------------------------------------------------
 
 
# #Step 7: Clear the GPIOs so that some other program might enjoy them
# #------------------------------------------------------------------------
# #------------------------------------------------------------------------
# #relase the GPIO
# #------------------------------------------------------------------------
# #------------------------------------------------------------------------