# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kitap_ekleme.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import *
import sys
import db_islemleri
from kitap_eklemeui import Ui_kitapKaydetmeFormu


class Kitap_Kaydetme_Ekrani(QWidget, Ui_kitapKaydetmeFormu):
    def __init__(self, user_id = 1):
        super(Kitap_Kaydetme_Ekrani, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app =QApplication(sys.argv)
    kitapKaydetmeFormu = Kitap_Kaydetme_Ekrani(1)
    kitapKaydetmeFormu.show()
    sys.exit(app.exec_())
