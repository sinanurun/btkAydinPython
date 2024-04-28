def o_karti(a,b,c = 18,*args,**kwargs):
    print(args)
    print(kwargs)
    o_bilgiler = {**kwargs}
    print(o_bilgiler)
o_karti(5,6,8,9,"YBS","Bilecik",o_adi="Esra",o_no=35,o_sehir="İzmir")