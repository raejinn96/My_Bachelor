from time import sleep

class Count():
    def hitungMundur():
        waktu = 7
        while waktu > 0:
            print(waktu)
            waktu -= 1
            sleep(1)
        print("Mulai")
