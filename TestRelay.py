import os
import RPi.GPIO as GPIO
from time import sleep
from google.cloud import firestore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/Skripsi_Fix/Program/skripsi-pembersih-firebase-adminsdk-iyyqn-64723bef17.json"
db = firestore.Client()

relay = 5
sigPin = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)
GPIO.setup(sigPin, GPIO.IN)

try:
    while True:
        # if GPIO.input(sigPin) == 1:
        #     print('Normal')
        #     sleep(1)
        # else:
        #     print('hujan')
        #     sleep(1)

        doc_ref = db.collection("weather").document("current_condition")
        doc_watch = doc_ref.on_snapshot(lambda doc_snapshot, changes, read_time: 
        [GPIO.output(relay, 0) if doc.get("cleaning") 
         else GPIO.output(relay, 1) for doc in doc_snapshot]
)
        sleep(2)  
                    

        # GPIO.output(relay, 1)
        # print(f"Relay is OFF")
        # sleep(5)
        # GPIO.output(relay, 0)
        # print(f"Relay is ON")
        # sleep(5)

finally:
    GPIO.cleanup()   
    print("clean up")     