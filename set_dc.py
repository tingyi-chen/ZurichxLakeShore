import sys
from PyQt5.QtWidgets import QMainWindow
from zurich import Zurich
from PyQt5 import uic
from ui.dc_ui import Ui_MainWindow

class SetDC(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(SetDC, self).__init__(parent)
        self.zurich = Zurich()
        uic.loadUi("ui/dc_ui.ui", self)
        self.setDC()
        
    def setDC(self):
        self.voltageOutRange.currentTextChanged.connect(self.zurich.setVoutRange)
