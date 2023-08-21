import RPi.GPIO as GPIO
from time import sleep
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Hujan:
    def __init__(self, sigPin, hujan):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sigPin, GPIO.IN)
        cred = credentials.Certificate("/home/pi/Skripsi_Fix/Program/skripsi-pembersih-firebase-adminsdk-iyyqn-64723bef17.json")
        firebase_admin.initialize_app(cred)
        
        
        self.db = firestore.client()
        self.sinyal = sigPin 
        self.hujan = hujan

    def cek(self):
        doc_ref = self.db.collection(u'weather').document(u'current_condition')
        doc_ref.update({u'itsraining' : self.hujan})


        baca = GPIO.input(self.sinyal)   
        if baca == 0:
            print("Hujan")
            sleep(1)
        else:
            print("Normal")
            sleep(1)
            
        return baca         

