#while döngüsü koşul geçerli olduğu sürece çalışır
cevap = input("pizza ister misiniz")
while cevap == "evet":
    print("pizzanız afiyet olsun")
    cevap = input("Bir dilim daha pizza ister misiniz")
    if cevap == "hayır":
        print("Bizi tercih ettiğiniz için teşekkürler")
