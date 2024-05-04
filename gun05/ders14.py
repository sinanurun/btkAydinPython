class Otomobil():
    def __init__(self,marka,model,renk):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.CalismaDurum = False

    def calistir(self):
        if self.CalismaDurum == False:
            self.CalismaDurum = True
            print(f"{self.marka} araba çalıştırıldı")
            self.hiz = 0
        else:
            print(f" {self.marka} Araba Zaten Çalışıyor")

    def durdur(self):
        if self.CalismaDurum == True:
            self.CalismaDurum = False
            print(f"{self.marka} araba durduruldu")
            self.hiz = 0
        else:
            print(f" {self.marka} Araba Zaten Duruyor")

    def hizArttir(self):
        if self.CalismaDurum == True:
            self.hiz += 10
        else:
            print(f" {self.marka} önce aracı çalıştırın")

    def hizAzalt(self):
        if self.CalismaDurum == True and self.hiz > 0:
            self.hiz -=10
        elif self.hiz == 0:
            print(f" {self.marka} araç çalışıyor ama zaten duruyor")
        else:
            print(f" {self.marka} araba zaten çalışmıyor")

    def __str__(self):
        return f'{self.marka}, {self.model} Otomobil'


oto1 = Otomobil("Ford","Focus","Gri")
oto1.calistir()
oto1.calistir()
print(oto1)
oto2 = Otomobil("Audi","A4","Kırmızı")
print(oto2)
print(oto2.CalismaDurum)
oto2.calistir()

