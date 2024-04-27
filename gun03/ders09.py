sayilar = []
for i in range(10):
    sayilar.append(int(input(f"{i+1}. sayıyı giriniz")))
# sayilar.sort()
# ek = sayilar[0]
# eb = sayilar[-1]
# print(ek, eb, sayilar)
eb = ek = sayilar[0]
for sayi in sayilar:
    if sayi > eb:
        eb = sayi
    if sayi < ek:
        ek = sayi
print(ek, eb, sayilar)