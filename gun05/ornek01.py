def sinif_ortalama(*args):
    toplam = 0
    for arg in args:
        toplam += arg
    return toplam/len(args)

print(sinif_ortalama(80,95,75,68,45,36,12))
