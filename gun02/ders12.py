#macth case
gun = int(input("Haftanın kaçıncı günü: "))
match gun:
    case 1:
        print("pazartesi")
    case 2:
        print("salı")
    case 3:
        print("Çarşamba")
    case _:
        print("Hatalı gün girişi yapıldı")