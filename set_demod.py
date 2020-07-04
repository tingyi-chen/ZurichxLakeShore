import sys
from PyQt5.QtWidgets import QMainWindow
from zurich import Zurich
from PyQt5 import uic
from ui.demod_ui import Ui_MainWindow

class SetDemod(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(SetDemod, self).__init__(parent)
        self.zurich = Zurich()
        uic.loadUi("ui/demod_ui.ui", self)
        self.setDemod()
        
    def setDemod(self):
        self.tc.setRange(0, 100)
        self.rate.setRange(0, 7000)
        self.order.setRange(1, 8)
        
        self.tc.setValue(10.16)
        self.rate.setValue(225)
        self.order.setValue(4)


        self.adcSelect.valueChanged.connect(self.zurich.setDemodsADCSelect)
        self.order.valueChanged.connect(self.zurich.setDemodsOrder)
        self.tc.valueChanged.connect(self.zurich.setDemodsTC)
        self.tc.setDecimals(4)
        self.rate.valueChanged.connect(self.zurich.setDemodsRate)

        