import datetime
from time import sleep, strftime
import time
import os

# try:
#     import ntplib
#     client = ntplib.NTPClient()
#     response = client.request('pool.ntp.org')
#     t = time.localtime()
#     # ntp = t.strftime("%m %d %H:%M:%S %Y")
#     print(t)
# except:
#     print('Could not sync with time server.')

# print('Done.')
 
# using now() to get current time
# sekarang = datetime.datetime.now()
# print(sekarang)
 
# Printing value of now.


# print(f"{hari}/{bulan}/{tahun}")
# print(f"{jam}:{menit}")

while True:

    sekarang = datetime.datetime.now()
    
    tahun = sekarang.year
    bulan = sekarang.month
    hari = sekarang.day
    jam = sekarang.hour
    menit = sekarang.minute

    print(f"{hari}/{bulan}")
    if menit % 2 == 0:
        print(f"{jam}:{menit} menit genap")
    else:
        print(f"{jam}:{menit} menit ganjil")  
    sleep(2)    
          
