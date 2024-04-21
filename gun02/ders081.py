# teşekkür takdir elif yapısı
puan = int(input("Puan : "))
if puan < 0:
    print("hatalı giriş ")
elif puan < 70 :
    print("Puan belge almaya yetmiyor")
elif puan <85 :
    print("Puan Teşekkür için yeterli")
elif puan <=100:
    print("Puan takdir için yeterli")
else:
    print("Puan hatalı girildi")