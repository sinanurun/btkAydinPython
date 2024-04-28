# dosya oluşturma ve içine veri yazma
metin = "\nçok faydalı bir kurs oluyor bizler icin"
dosya = open("deneme.txt","a")
dosya.write(metin)
dosya.close()