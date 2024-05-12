# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anaekran.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import *
import sys
from anaekranui import Ui_MainWindow
from db_islemleri import *
from kitap_ekleme import *

class AnaEkran(QMainWindow, Ui_MainWindow):
   def __init__(self, user_id = 1):
       super(AnaEkran, self).__init__()
       self.user_id = user_id

       self.karsilama()

   def karsilama(self):
       self.setupUi(self)

       self.actionKitaplarim.triggered.connect(self.karsilama)
       self.actionKitap_Ekle.triggered.connect(self.kitap_ekle)
       self.kitap_tablosu_olustur()


   def kitap_ekle(self):
       self.setCentralWidget(Kitap_Kaydetme_Ekrani(self.user_id))

   def kitap_tablosu_olustur(self):
       kitaplar = kitap_listele(self.user_id)
       try:
           if kitaplar != False:
               for index, kitap in enumerate(kitaplar):
                   self.kitapTablosu.insertRow(index)
                   self.kitapTablosu.setItem(index,0,QTableWidgetItem(str(kitap.kitap_id)))
                   self.kitapTablosu.setItem(index,1,QTableWidgetItem(kitap.kitap_adi))
                   self.kitapTablosu.setItem(index,2,QTableWidgetItem(str(kitap.kitap_sayfa_sayisi)))
       except:
           pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    anaekran = AnaEkran(1)
    anaekran.show()
    sys.exit(app.exec_())
