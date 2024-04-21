ad1 = "ali"
ad2 = "veli"
ad3 = "can"
print(f"{ad1} {ad2} {ad3}")
metin = "Merhaba {} Kursumuza Hoşgeldin"
print(metin.format(ad1))
print(metin.format(ad2))
print(metin.format(ad3))

metin2 = "Merhaba Yarışma listesi {} {} {}"
print(metin2.format(ad3, ad2, ad1))

metin3="{k1}, {k2}, {k3} hoşgeldiniz".format(k1=ad2,k2=ad1,k3=ad3)
print(metin3)