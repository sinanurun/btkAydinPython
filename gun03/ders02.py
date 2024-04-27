ogrenci_ad = input("adınızı giriniz")
ogrenci_soyadi = "Kaçar"
ogrenci_yas = 27
ogrenci_boy = 1.6
ogrenci_cinsiyet = True

ogrenci = [ogrenci_ad,ogrenci_soyadi,ogrenci_yas,ogrenci_boy,ogrenci_cinsiyet]
print(ogrenci)
# print(type(ogrenci))
print(len(ogrenci))
print(ogrenci[0])
print(type(ogrenci[0]))
print(ogrenci[-1])
print(ogrenci[:2])
for dd in ogrenci:
    print(dd)