gorevler = []
while True:
    gorev = input("Gorev Giriniz veya X'e Basınız: ")
    if gorev.lower() == "x":
        print("Görev Girişi Tamamlandı")
        break
    else:
        gorevler.append(gorev)
print(gorevler)
while gorevler != []:
    for dd in range(len(gorevler)):
        durum = input(f"{gorevler[dd]} görevini yaptınız mı ? e - h" )
        if durum == "e":
            gorevler.pop(dd)
            break
else:
    print("Tüm Görevler Tamamlandı")