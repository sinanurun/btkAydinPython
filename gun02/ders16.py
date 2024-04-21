#for döngüsü kaç kere çalışacağı belli olan yapılar için kullanılır
print(list(range(5,10)))
for i in range(5,10):
    print(i, end=" - ")


isim = "sevgi"
for harf in isim:
    print(harf, end=",")
