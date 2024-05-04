class Ogrenci():
    bolum = "Maliye"
    bina = "Kuzey"
    def __init__(self, ad, soyad, tcno):
        self.ad = ad
        self.soyad = soyad
        self.tcno = tcno

    def tamad(self):
        self.tam_isim = self.ad + self.soyad
        return self.tam_isim
    def __str__(self):
        return self.ad + self.soyad

ogr1 = Ogrenci("Sevgi","Can","12541254")
print(ogr1)
ogr1.tamad()
print(ogr1.tam_isim)
ogr2 = Ogrenci("Berk","Veli","87878784")
print(ogr2)
ogr2.tamad()
print(ogr2.tam_isim)




