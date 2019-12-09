import sys
from PyQt5.QtWidgets import QMainWindow
from zurich import Zurich
from PyQt5 import uic
from ui.in_ui import Ui_MainWindow

class SetIn(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(SetIn, self).__init__(parent)
        self.zurich = Zurich('dev1521', 0)
        uic.loadUi("ui/in_ui.ui", self)
        self.setIn()
        

    def setIn(self):
        '''設定訊號輸入的 UI 與程式之間的連結。'''
        self.voltageInRange.setSingleStep(0.1)
        self.voltageInRange.setValue(1.2)
        self.voltageInRange.setRange(0.1, 2)
        self.voltageInRange.valueChanged.connect(self.zurich.setVinRange)
        self.diffYes.clicked.connect(self.zurich.setDiffYes)
        self.diffNo.clicked.connect(self.zurich.setDiffNo)
        self.imp50Yes.clicked.connect(self.zurich.setImp50Yes)
        self.imp50No.clicked.connect(self.zurich.setImp50No)
        self.acCouplingYes_ZI.clicked.connect(self.zurich.setACCouplingYes_ZI)
        self.acCouplingNo_ZI.clicked.connect(self.zurich.setACCouplingNo_ZI)
