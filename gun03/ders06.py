# iç içe listeler, çok boyutlu listeler
sebze = ['domates', 'biber']
meyve = ['üzüm', 'çilek', 'kivi', 'karpuz', 'incir', 'ayva', 'armut', 'armut']
sark = ["peynir", "helva", "bal"]
yesillik = ["roka", "maydanoz", "tere"]
# pazar_listesi = sebze + meyve + sark + yesillik
# print(pazar_listesi)
# print(len(pazar_listesi))
pazar_listesi = [sebze, meyve, sark,yesillik, "baklava"]
print(pazar_listesi)
print(len(pazar_listesi))
print(pazar_listesi[0][0])
print(pazar_listesi[1][2])
for kategori in pazar_listesi:
    print(kategori)
    if type(kategori) is list:
        for urun in kategori:
            print(urun)
    else:
        print(kategori)