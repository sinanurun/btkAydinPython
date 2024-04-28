import random
rastgele = random.randrange(1,1000)
print("tutulan sayı",rastgele)
tahminSayisi = 10
taban = 0
tavan = 1001
while tahminSayisi >= 1:
    tahmin =random.randrange(taban,tavan)
    print(tahmin , end=" ")
    if tahmin == rastgele:
        print("Tebrikler")
        break
    elif tahmin > rastgele:
        tavan = tahmin
    elif tahmin < rastgele:
        taban = tahmin
    tahminSayisi -= 1
    print("kalan hakkınız", tahminSayisi)