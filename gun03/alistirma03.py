# * lardan kare yapımı
"""
kare_kenari = int(input("Kare keranı giriniz:"))
for a in range(kare_kenari):
    for b in range(kare_kenari):
        print("*", end="")
    print()
"""
# Dikdörgen şeklinde * yazdıran
kenar1 = int(input("Kenar1 giriniz:"))
kenar2 = int(input("Kenar2 giriniz:"))
for satir in range(kenar1):
    for sutun in range(kenar2):
        print("*", end="")
    print()