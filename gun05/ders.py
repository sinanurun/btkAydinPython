from math import sqrt
import os
def asal(n):
    kok=round(sqrt(n))+1
    kontol = 0
    for deneme in range(2,kok):
        if n % deneme ==0:
            kontol += 1
    # return True if kontol ==0 else False
    if kontol == 0:
        return True
    else:
        return False
def main():
 en_buyuk=int(input("Asal sayıları hangi değere kadar gösterelim? "))
 for deger in range(2,en_buyuk+1):
    if asal(deger):
        print(deger,end=" ")
print()
if __name__ == "__main__":
    main()
    os.system('cls' if os.name == 'nt' else 'clear')