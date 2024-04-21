#otoyol hız ceva kontrol uygulaması
yol = float(input("Kaç Km Yol  Gittiniz : "))
zaman = float(input("Kaç saat Yol  Gittiniz : "))
hiz = yol / zaman
hcb = 132
if hiz > hcb:
    print("cezayı yedin")
    print(f"{hiz-132} kadar ihlal ettiniz")
else:
    print("hız kurallarına uygun \ntebrikler")