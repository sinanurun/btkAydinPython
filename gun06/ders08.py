import json
kitap_listesi = []
class Kitap():
    def __init__(self,ad,yazar,sayfa,basim):
        self.ad=ad
        self.yazar=yazar
        self.sayfa=sayfa
        self.basim=basim

def kitapListesineEkle(kitap):
    degerler = vars(kitap)
    kitap_listesi.append(degerler)

def kitapListesiKaydet():
    y = json.dumps(kitap_listesi)
    with open("kitap.json","w") as file:
        file.write(y)

# kitap = Kitap("Python","Sinan Hoca",30, 2024)
#
# kitap_ekleme = kitapekle(kitap)
# if kitap_ekleme:
#     print("Kitap Ekleme Başarılı")
# else:
#     print("Kitap ekleme Başarısız")