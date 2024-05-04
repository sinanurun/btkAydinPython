
def for_dongusu(baslangic,bitis=0,artis=1):
    for_listesi = []
    def buyuyen(baslangic=baslangic,bitis=bitis,artis=artis):
        if baslangic < bitis:
            for_listesi.append(baslangic)
            return buyuyen(baslangic + artis, bitis, artis)
        else:
            return for_listesi
    def kuculen(baslangic=baslangic,bitis=bitis,artis=artis):
        if baslangic > bitis:
            for_listesi.append(baslangic)
            return kuculen(baslangic - artis, bitis, artis)
        else:
            return for_listesi

    if baslangic > bitis:
        return kuculen(baslangic,bitis,artis)
    else:
        return buyuyen(baslangic,bitis,artis)



print(for_dongusu(82,15,2))