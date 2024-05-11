import sys
from ekran1_ui import Ui_Form
from PyQt5.QtWidgets import *

class AnaEkranPenceresi(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = AnaEkranPenceresi()
    pencere.show()
    sys.exit(app.exec_())
