carpim = 1
adet = 0
while True:
    sayi = int(input("Bir sayı giriniz"))
    if sayi == 0:
        print("giridğiniz işleme tabi değil")
        continue
    carpim *= sayi
    adet += 1
    print(adet,". sayı",sayi)
    if adet == 10:
        print("Sayı girme işlemi tamamlandı")
        break
print(carpim)