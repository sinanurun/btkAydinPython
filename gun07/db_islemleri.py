from orm_db import *

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def birim_listele():
    birimler = session.query(Birim).all()
    print(birimler)

birim_listele()