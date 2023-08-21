import RPi.GPIO as GPIO
import os
import datetime
from time import sleep
from google.cloud import firestore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/Skripsi_Fix/Program/skripsi-pembersih-firebase-adminsdk-iyyqn-64723bef17.json"
db = firestore.Client()

from picamera import PiCamera
from Motor import Step
from Solenoid import Solenoid
from Rain import Hujan
from CountTo1 import Count

# pinout limit switch :
limit1 = 23
limit2 = 24
# pinout fungsi motor:
en = 17
dir = 27
pul = 22
# pinout fungsi sensor hujan:
rainPin = 16
# pinout fungsi solenoid valve:
solePin = 5


step = Step(en, dir, pul, limit1, limit2)  
hujan_detector = Hujan(rainPin, False)

solenoid = Solenoid(solePin)


try:
   
    # sleep(3)
    Count.hitungMundur()
    isCleaning = False
    camera = PiCamera(
        resolution=(1024, 768),)
    # step = Step(en, dir, pul, limit1, limit2)  
    # step.boleh()       

    while True:
        
        doc_ref = db.collection("weather").document("current_condition")
        doc = doc_ref.get()
        

# jadwal :
        sekarang = datetime.datetime.now() #fungsi waktu
        jam = sekarang.hour
        menit = sekarang.minute

        

        if jam == 7 and menit == 00:
            camera.capture()
            camera.led = True
            camera.rotation = 180
            camera.close()
        else:
            camera.close()    

        if jam == 9 and menit == 00:
            step.go()
        else:
            step.stop()    


        if doc.exists:
            cleaning_status = doc.get("cleaning")
            if cleaning_status:
                print("Cleaning is ON")
                # Start motor here or perform other cleaning actions
                step.go(isCleaning=True)
                # You can also start solenoid or other actions here
            else:
                print("Cleaning is OFF")
                # Stop motor here or perform other actions if needed
                step.stop()
        # solenoid.nyala()
        # hujan_detector.cek()
        
        
        
except KeyboardInterrupt:     
    print("\nIntrupsi") 

finally:
    GPIO.cleanup()
    print("clear")


