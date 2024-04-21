# ehliyet alma durumu
d_yili = int(input("Doğum Yılınızı Giriniz"))
yas = 2024 - d_yili
if yas >= 18 :
    print("Ehliyet Alabilirsiniz")
else:
    print("Ehliyet Alamazsınız")
    print(f"{18-yas} yıl daha beklemelisin")