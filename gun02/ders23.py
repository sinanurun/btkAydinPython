#while döngüsü koşul geçerli olduğu sürece çalışır
adet = int(input("kaç dilim pizza istersiniz"))
# while 0 < adet:
#     adet -= 1
#     print("pizza")

#versiyon 2
i = 0
while i < adet:
    i += 1
    print(i,".dilim pizzanız")