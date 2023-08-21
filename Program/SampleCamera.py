from time import sleep
from picamera import PiCamera



def ambil():
    folder = '/home/pi/Skripsi_Fix/images/bersih'
    filename = f"{folder}/bersih4.jpg"
    
    camera = PiCamera(
        resolution=(1024, 768),
        )
    
    camera.rotation = 180
    camera.led = True
    # camera.annotate_text = 'Hello!' # ngasih teks di dalam gambar
    print("printing 4")
    sleep(15)
    camera.capture(filename)
    camera.close()
    

ambil()

