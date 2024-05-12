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