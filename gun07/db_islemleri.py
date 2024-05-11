from orm_db import *

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def birim_listele():
    birimler = session.query(Birim).all()
    print(birimler)

def birim_ekle():
    b_adi = input("Eklenecek Birim Adını Giriniz")
    yeni_birim = Birim(birim_adi=b_adi)
    session.add(yeni_birim)
    session.commit()

def birim_sil():
    b_id = int(input("Bir ID Giriniz"))
    try:
        session.query(Birim).filter(Birim.birim_id==b_id).delete()
        session.commit()
    except:
        print("Geçersiz id Girdiniz")

birim_listele()
birim_ekle()
birim_listele()
birim_sil()
birim_listele()

