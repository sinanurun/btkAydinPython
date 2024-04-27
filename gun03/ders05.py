#versiyon 1
"""adet = int(input("Kaç adet zerzevat alacaksınız"))
zerzevat = [] #list()
for i in range(adet):
    urun = input(f"{i+1}. ürünü giriniz")
    zerzevat.append(urun)

print("Pazar Listeniz : ", zerzevat)"""

#versiyon 2
mesaj = """
Pazar Listesi Programına Hoşgeldiniz
Programdan Çıkmak için x'e basınız"""
print(mesaj)
zerzevat = []
while True:
    urun = input("Ürün girişi yapın veya X'e basın")
    if urun.lower() == "x":
        print("Pazar Listesi:",zerzevat)
        break
    else:
        zerzevat.append(urun)

