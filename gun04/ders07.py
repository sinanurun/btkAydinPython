dosya_Adi = "deneme.txt"
# with open(dosya_Adi) as dosya:
#     print(dosya.readline())

dosya = open(dosya_Adi)
metin = dosya.read()
print(metin)
satirlar = metin.split("\n")
print(satirlar)
