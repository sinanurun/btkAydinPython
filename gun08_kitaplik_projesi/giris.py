# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import *
import sys
from girisui import Ui_Giris_Formu
import db_islemleri
from anaekran import *

class Giris_Formu(QWidget, Ui_Giris_Formu):
    def __init__(self):
        super(Giris_Formu, self).__init__()
        self.setupUi(self)
        self.girisButonu.clicked.connect(self.giris_kontrol)

    def giris_kontrol(self):
        k_adi = self.kAdiEdit.text()
        k_sifre =self.kSifreEdit.text()
        user = db_islemleri.k_girisi(k_adi,k_sifre)
        if user != 0 :
            print("oturum açan kullanıcı idsi:",user)
            self.hide()
            self.yekran = AnaEkran(user)
            self.yekran.show()
        else:
            print("oturum açma işlemi gerçekleşmedi")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    giris_ekrani = Giris_Formu()
    giris_ekrani.show()
    sys.exit(app.exec_())
