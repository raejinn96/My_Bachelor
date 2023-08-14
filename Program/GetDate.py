from time import strftime
from time import sleep


try:
    while True:
        tanggal = strftime("%d/%m/%y" )
        jam = strftime("%H:%M")
        if jam == "17:30":
            print(f"Sekarang Tanggal: {tanggal}\nJam: {jam}\n")
            print("Waktunya")
            sleep(1)
        else:
            print(f"Sekarang Tanggal: {tanggal}\nJam: {jam}\n")
            print("Belum")  
            sleep(1)   
except KeyboardInterrupt:
    print("Interrupted")
finally:
    print("Done")           