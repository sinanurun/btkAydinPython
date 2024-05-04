import random
import os

def oyun(dosya_adi):
    dosya = open(dosya_adi, "a")
    rastgele = random.randrange(1, 100)
    dosya.write(str(rastgele) + " + ")
    tahminSayisi = 10
    taban = 0
    tavan = 100
    while tahminSayisi >= 1:
        tahmin = int(input("Bir Sayı Giriniz"))
        dosya.write(str(tahmin) + ",")
        if tahmin == rastgele:
            dosya.write("+ kazandınız \n")
            print("Tebrikler Kazandınız")
            dosya.close()
            break
        elif tahmin > rastgele:
            print("daha küçük bir değer giriniz")
            tavan = tahmin
        elif tahmin < rastgele:
            print("daha büyük bir sayı giriniz")
            taban = tahmin
        tahminSayisi -= 1
        print("kalan tahmin sayınız", tahminSayisi)
        if tahminSayisi == 0:
            dosya.write("Kaybettiniz \n")
            dosya.close()

def istatistik(dosya_adi):
    dosya = open(dosya_adi)
    print(dosya.read())
    print(dosya.readlines())
    dosya.close()
def dosya_kontrol(dosya_adi):
    if not (os.path.exists(dosya_adi)):
        dosya = open(dosya_adi, "x")
        dosya.close()
def cikis():
    print("Programdan Çıkış Yapıldı")
    exit()
def menu():
    cevap = int(input("oyun için 1,\tİstatistik için 2,\tÇıkış için 3"))
    return cevap

def main():
    while True:
        dosya_adi = "oyun.txt"
        dosya_kontrol(dosya_adi)
        kgirisi = menu()
        if kgirisi == 3:
            cikis()
        elif kgirisi == 1:
            oyun(dosya_adi)
        elif kgirisi == 2:
            istatistik(dosya_adi)

if __name__ == "__main__":
    main()