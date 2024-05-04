

def ikinci():
    print("çalışan ikinci fonskiyon")

def ucuncu():
    print("Ucuncu fonksiyon")
    return 5

def birinci():
    print("Birinci Çalışacak fonksiyon ")
    ikinci()
    return ucuncu()

if __name__ == "__main__":
    print("Hello")
    a = birinci()
    print(a)