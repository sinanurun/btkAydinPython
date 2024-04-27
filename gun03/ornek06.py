# bolum 4 soru 20 amstrong sayısı işlemi
# sayi = int(input("bir sayı giriniz: "))
# ssayi = str(sayi)
# toplam = 0
# for rakam in ssayi:
#     kup = int(rakam) ** len(ssayi)
#     toplam += kup
#     print(rakam,kup,toplam)
# if toplam == sayi:
#     print(sayi," sayısı bir amstrong sayısıdır")
# else:
#     print(sayi," sayısı bir amstrong sayısı değildir")

#versiyon 2
# # bolum 4 soru 20 amstrong sayısı işlemi
# baslangic = int(input("Baslangic: "))
# bitis = int(input("Bitis: "))
# adet = 0
# for sayi in range(baslangic,bitis):
#     ssayi = str(sayi)
#     toplam = 0
#     for rakam in ssayi:
#         kup = int(rakam) ** len(ssayi)
#         toplam += kup
#         # print(rakam,kup,toplam)
#     if toplam == sayi:
#         print(sayi," sayısı bir amstrong sayısıdır")
#         adet +=1
#     else:
#         continue
#         print(sayi," sayısı bir amstrong sayısı değildir")
# print(f"{baslangic}-{bitis} aralığında {adet} amstrong var")

# bolum 4 soru 20 amstrong sayısı işlemi
for a in range(1,11):
    sayi = int(input(f"{a}. deneme için bir sayı giriniz: "))
    ssayi = str(sayi)
    toplam = 0
    for rakam in ssayi:
        kup = int(rakam) ** len(ssayi)
        toplam += kup
        print(rakam,kup,toplam)
    if toplam == sayi:
        print(sayi," sayısı bir amstrong sayısıdır")
        break
    else:
        print(sayi," sayısı bir amstrong sayısı değildir")