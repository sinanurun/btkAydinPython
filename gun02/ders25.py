bas = int(input("başlangıç değerini giriniz"))
bitis = int(input("bitiş değerini giriniz"))
artis = int(input("artis değerini giriniz"))
toplam = 0
while bas < bitis:
    print(bas, end=" - ")
    toplam += bas
    bas += artis
    print(toplam)
else:
    print("Hesaplama Tamamlanmıştır")
print("Girilen sayıların toplamı",toplam)