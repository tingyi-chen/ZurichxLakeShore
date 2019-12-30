import sys
from PyQt5.QtWidgets import QMainWindow
from zurich import Zurich
from PyQt5 import uic
from ui.in_ui import Ui_MainWindow

class SetIn(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(SetIn, self).__init__(parent)
        self.zurich = Zurich('dev1521', 0, 'GPIB0::12::INSTR')
        uic.loadUi("ui/in_ui.ui", self)
        self.setIn()
        

    def setIn(self):
        '''設定訊號輸入的 UI 與程式之間的連結。'''
        self.Channel1.clicked.connect(self.zurich.setInChannel_1)
        self.Channel2.clicked.connect(self.zurich.setInChannel_2)
        
        self.voltageInRange_1.setSingleStep(0.1)
        self.voltageInRange_1.setValue(1.2)
        self.voltageInRange_1.setRange(0.01, 2)
        self.voltageInRange_1.valueChanged.connect(self.zurich.setVinRange)
        self.diffYes_1.clicked.connect(self.zurich.setDiffYes)
        self.diffNo_1.clicked.connect(self.zurich.setDiffNo)
        self.imp50Yes_1.clicked.connect(self.zurich.setImp50Yes)
        self.imp50No_1.clicked.connect(self.zurich.setImp50No)
        self.acCouplingYes_ZI_1.clicked.connect(self.zurich.setACCouplingYes_ZI)
        self.acCouplingNo_ZI_1.clicked.connect(self.zurich.setACCouplingNo_ZI)

        self.voltageInRange_2.setSingleStep(0.1)
        self.voltageInRange_2.setValue(1.2)
        self.voltageInRange_2.setRange(0.01, 2)
        self.voltageInRange_2.valueChanged.connect(self.zurich.setVinRange)
        self.diffYes_2.clicked.connect(self.zurich.setDiffYes)
        self.diffNo_2.clicked.connect(self.zurich.setDiffNo)
        self.imp50Yes_2.clicked.connect(self.zurich.setImp50Yes)
        self.imp50No_2.clicked.connect(self.zurich.setImp50No)
        self.acCouplingYes_ZI_2.clicked.connect(self.zurich.setACCouplingYes_ZI)
        self.acCouplingNo_ZI_2.clicked.connect(self.zurich.setACCouplingNo_ZI)
