import json
kitap_listesi = []
kitaplar = []
class Kitap():
    def __init__(self,ad,yazar,sayfa,basim):
        self.ad=ad
        self.yazar=yazar
        self.sayfa=sayfa
        self.basim=basim
    def __str__(self):
        return self.ad

def kitapListesineEkle():
    kitap_adi = input("Kitap adı")
    kitap_yazar = input("yazar")
    kitap_sayfa = int(input("sayfa"))
    kitap_yili = int(input("yili"))
    kitap = Kitap(kitap_adi,kitap_yazar, kitap_sayfa, kitap_yili)
    degerler = vars(kitap)
    kitap_listesi.append(degerler)
    kitaplar.append(kitap)

def kitapListesiKaydet():
    y = json.dumps(kitap_listesi)
    with open("kitap.json","w") as file:
        file.write(y)
    kitap_listesi.clear()
    kitaplar.clear()

def kitapListele():
    if len(kitaplar)>0:
        for kitap in kitaplar:
            print(kitap)
    else:
        print("Kaydedilmeyi bekleyen kitap yok")
def menu():
    k_giris = input("Kaydet, Ekle, Çıkart, Listele, Dosya listele, Q")
    return k_giris
while True:
    cevap = menu()
    if cevap == "e":
        kitapListesineEkle()
    elif cevap == "k":
        kitapListesiKaydet()
    elif cevap == "q":
        print("programdan çıkıldı")
        exit()
    elif cevap == "l":
        pass
    elif cevap == "d":
        pass
    else:
        print("hatalı işlem girişi")

# kitap = Kitap("Python","Sinan Hoca",30, 2024)
#
# kitap_ekleme = kitapekle(kitap)
# if kitap_ekleme:
#     print("Kitap Ekleme Başarılı")
# else:
#     print("Kitap ekleme Başarısız")