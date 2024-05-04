class Ogrenci():
    kurs = "BTK"
    fakulte = ""


print(Ogrenci().kurs)
ogr1 = Ogrenci()
ogr1.fakulte = "Siyasal Bilgiler Fakultesi"
print(ogr1.kurs, ogr1.fakulte)

ogr2 = Ogrenci()
ogr2.kurs = "GSB"
print(ogr2.kurs)
print(Ogrenci().kurs)