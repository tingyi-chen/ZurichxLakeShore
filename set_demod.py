import sys
from PyQt5.QtWidgets import QMainWindow
from zurich import Zurich
from PyQt5 import uic
from ui.demod_ui import Ui_MainWindow

class SetDemod(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(SetDemod, self).__init__(parent)
        self.zurich = Zurich('dev1521', 0)
        uic.loadUi("ui/demod_ui.ui", self)
        self.setDemod()
        
    def setDemod(self):
        self.adcSelect.valueChanged.connect(self.zurich.setDemodsADCSelect)
        self.order.valueChanged.connect(self.zurich.setDemodsOrder)
        self.tc.valueChanged.connect(self.zurich.setDemodsTC)
        self.rate.valueChanged.connect(self.zurich.setDemodsRate)
