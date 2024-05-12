from orm_db import *

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def k_girisi(k_adi, k_sifre):
    try:
        kullanici = (session.query(User).
                     filter(User.user_adi==k_adi,User.user_sifre==k_sifre)
                     .first())
        return kullanici.user_id
    except:
        return 0

def kitap_listele(k_id):
    try:
        kitaplar = session.query(Kitaplik).filter(Kitaplik.kitap_user==k_id).all()
        if len(kitaplar) > 0:
            return kitaplar
        else:
            return False
    except:
        return False

def kitap_ekle(k_adi,k_sayfa_sayisi,user_id):
    try:
        yeni_kitap = Kitaplik(kitap_user=user_id,kitap_adi=k_adi,kitap_sayfa_sayisi=int(k_sayfa_sayisi))
        session.add(yeni_kitap)
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False