# geçerli mail adresi kontrolü yapan uygulama
mail = input("Mail adresinizi giriniz : ")
if "@" in mail:
    print("Mail adresiniz geçerli")
else:
    print("Mail adresiniz geçersiz")

# geçerli mail adresi girilene kadar mail adresi isteyen
while True:
    mail = input("Mail adresinizi giriniz : ")
    if "@" in mail:
        print("Mail adresiniz geçerli")
        break
    else:
        print("Mail adresiniz geçersiz")
