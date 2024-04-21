#yemek sipariş and or içiçe koşullu ifadeler
yemek = input("Yemek Bilgisi Giriniz : ")
if yemek == "pide":
    icecek = input("icecek giriniz")
    if icecek == "kola":
        print("geçerli siprariş")
    else:
        print("yiyecek doğru ama içeçek yanlış")
else:
    print("hatalı yemek siparişi")