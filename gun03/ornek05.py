#versiyon 1 kullanıcıdan sayı aldık kontrol ettik

"""sayi = 55
tahmin = int(input("Sayı giriniz"))
if tahmin == sayi:
    print("Tahmininiz Doğru Tebrikler")
else:
    print("Tahmininiz Hatalı")"""
# versiyon2
# sayi = 55
# tahmin = int(input("Sayı giriniz"))
# if tahmin == sayi:
#     print("Tahmininiz Doğru Tebrikler")
# elif tahmin > sayi:
#     print("Tahmininiz Hatalı keşke küçük deseydin")
# elif tahmin < sayi:
#     print("Tahmininiz Hatalı keşke büyük deseydin")

# #verisyon 3 aralık belirtme
# sayi = 55
# print("Tahmininiz edeceğiniz sayı 0 - 100 aralığındadır")
# taban = 0
# tavan = 100
# tahmin = int(input("Sayı giriniz"))
# while True:
#     if taban < tahmin < tavan:
#         print("Tahmininiz geçerli")
#         break
#     else:
#         print("geçersiz aralıkta değer girdiniz")
#         tahmin = int(input("Yeni sayı giriniz"))
# if tahmin == sayi:
#     print("Tahmininiz Doğru Tebrikler")
# elif tahmin > sayi:
#     print("Tahmininiz Hatalı keşke küçük deseydin")
# elif tahmin < sayi:
#     print("Tahmininiz Hatalı keşke büyük deseydin")

# #verisyon 4 tahmin etmeye devam edebilsin
# sayi = 55
# print("Tahmininiz edeceğiniz sayı 0 - 100 aralığındadır")
# taban = 0
# tavan = 100
# tahmin = int(input("Sayı giriniz"))
# while True:
#     if taban < tahmin < tavan:
#         print("Tahmininiz geçerli")
#         break
#     else:
#         print("geçersiz aralıkta değer girdiniz")
#         tahmin = int(input("Yeni sayı giriniz"))
# while True:
#     if tahmin == sayi:
#         print("Tahmininiz Doğru Tebrikler")
#         break
#     elif tahmin > sayi:
#         tahmin = int(input("Tahmin Hatalı daha küçük sayı :"))
#     elif tahmin < sayi:
#         tahmin = int(input("Tahmin Hatalı daha büyük sayı: "))
#

#5 tahmin etmeye devam edebilsin ama aralıkta
sayi = 55
print("Tahmininiz edeceğiniz sayı 0 - 100 aralığındadır")
taban = 0
tavan = 100
tahmin = int(input("Sayı giriniz"))
while True:
    if taban < tahmin < tavan:
        print("Tahmininiz geçerli")
        break
    else:
        print("geçersiz aralıkta değer girdiniz ")
        tahmin = int(input(f"Yeni sayı giriniz {taban}-{tavan} : "))

while tahmin != sayi: # not(tahmin == sayi)
    if tahmin > sayi:
        tavan = tahmin
        tahmin = int(input("Tahmin Hatalı daha küçük sayı :"))
        while True:
            if taban < tahmin < tavan:
                print("Tahmininiz geçerli")
                break
            else:
                print(f"geçerli aralıkta değer giriniz {taban}-{tavan}")
                tahmin = int(input(f"Yeni sayı giriniz {taban}-{tavan} : "))
    elif tahmin < sayi:
        taban = tahmin
        tahmin = int(input("Tahmin Hatalı daha büyük sayı: "))
        while True:
            if taban < tahmin < tavan:
                print("Tahmininiz geçerli")
                break
            else:
                print(f"geçerli aralıkta değer giriniz {taban}-{tavan}")
                tahmin = int(input(f"Yeni sayı giriniz {taban}-{tavan} : "))
else:
    print("Tahmininiz Doğru oldu Tebrikler")

