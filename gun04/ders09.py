import random
import os

dosya_adi = "oyun.txt"
if not (os.path.exists(dosya_adi)):
    dosya = open(dosya_adi, "x")
    dosya.close()

while True:
    cevap = int(input("oyun için 1,\tİstatistik için 2,\tÇıkış için 3"))
    if cevap == 1:
        pass
    elif cevap == 2:
        dosya = open(dosya_adi)
        print(dosya.readlines())
        dosya.close()
    else: # elif cevap == 3:
        print("Sistemden Çıkış Yapıldı")
        break