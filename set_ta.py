import sys
from PyQt5.QtWidgets import QMainWindow
from zurich import Zurich
from PyQt5 import uic
from ui.ta_ui import Ui_MainWindow

class SetTA(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(SetTA, self).__init__(parent)
        self.zurich = Zurich('dev1521', 0, 'GPIB0::12::INSTR')
        uic.loadUi("ui/ta_ui.ui", self)
        self.ta()
        
    def ta(self):
        self.gainValue.currentTextChanged.connect(self.zurich.setGain)
        self.acCouplingYes_TA.clicked.connect(self.zurich.setTAdccouplingNo)
        self.acCouplingNo_TA.clicked.connect(self.zurich.setTAdccouplingYes)
