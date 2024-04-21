# teşekkür takdir iç içe if yapısı
puan = int(input("Puan : "))
if puan < 70 :
    print("Puan belge almaya yetmiyor")
else:
    if puan <85 :
        print("Puan Teşekkür için yeterli")
    else:
        if puan <=100:
            print("Puan takdir için yeterli")
        else:
            print("Puan hatalı girildi")