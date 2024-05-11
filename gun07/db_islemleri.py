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

birim_listele()
birim_ekle()
birim_listele()

