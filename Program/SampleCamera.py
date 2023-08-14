from time import sleep
from picamera import PiCamera
from fractions import Fraction


def ambil():
    folder = '/home/pi/Skripsi_Fix/images/kotor'
    filename = f"{folder}/kotor60.jpg"
    
    camera = PiCamera(
        resolution=(1024, 768),
        # resolution=(640, 480) 
        )
    
    camera.rotation = 180
    camera.led = True
    # camera.annotate_text = 'Hello!' # ngasih teks di dalam gambar
    print("printing 60")
    sleep(15)
    camera.capture(filename)
    camera.close()
    
# Give the camera a good long time to set gains and
# measure AWB (you may wish to use fixed AWB instead)

ambil()

