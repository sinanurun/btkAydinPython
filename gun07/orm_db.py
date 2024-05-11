#veri tabanı oluşturma
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *  #tablolar arası ilişki kurmak için
from sqlalchemy import *

Base = declarative_base()
class Birim(Base):
    __tablename__ = 'birim'

    birim_id = Column(Integer, primary_key=True,autoincrement=True)
    birim_adi = Column(String(100), nullable=False)

    def __repr__(self):
        return f'{self.birim_id} - {self.birim_adi}'

engine = create_engine('sqlite:///deneme.sqlite')
Base.metadata.create_all(engine)