import RPi.GPIO as GPIO
import os
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
    # step = Step(en, dir, pul, limit1, limit2)  
    # step.boleh()       

    while True:
        
        # solenoid.nyala()
        # hujan_detector.cek()
        print("wey")
        sleep(1)
        
        doc_ref = db.collection("weather").document("current_condition")
        doc_watch = doc_ref.on_snapshot(lambda doc_snapshot, changes, read_time: 
        [solenoid.nyala() if doc.get("cleaning") 
         else solenoid.mati() for doc in doc_snapshot])
            
    
            # break
    
        
        
        
except KeyboardInterrupt:     
    print("\nIntrupsi") 

finally:
    GPIO.cleanup()
    print("clear")


