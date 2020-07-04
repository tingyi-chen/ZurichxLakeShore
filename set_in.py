import sys
from PyQt5.QtWidgets import QMainWindow
from zurich import Zurich
from PyQt5 import uic
from ui.in_ui import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def clickable(widget):

    class Filter(QObject):

        clicked = pyqtSignal()

        def eventFilter(self, obj, event):

            if obj == widget:
                if event.type() == QEvent.MouseButtonPress:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
             
                return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

class SetIn(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(SetIn, self).__init__(parent)
        self.zurich = Zurich()
        uic.loadUi("ui/in_ui.ui", self)
        self.setIn()
    
    def setIn(self):
        '''設定訊號輸入的 UI 與程式之間的連結。'''

        self.voltageInRange_1.setSingleStep(0.1)
        self.voltageInRange_1.setValue(1.2)
        self.voltageInRange_1.setRange(0.01, 2)
        self.voltageInRange_1.valueChanged.connect(self.zurich.setVinRange)
        self.diffNo.setChecked(True)
        self.diffYes.clicked.connect(self.zurich.setDiffYes)
        self.diffNo.clicked.connect(self.zurich.setDiffNo)
        self.imp50No.setChecked(True)
        self.imp50Yes.clicked.connect(self.zurich.setImp50Yes)
        self.imp50No.clicked.connect(self.zurich.setImp50No)
        self.acCouplingYes_ZI.setChecked(True)
        self.acCouplingYes_ZI.clicked.connect(self.zurich.setACCouplingYes_ZI)
        self.acCouplingNo_ZI.clicked.connect(self.zurich.setACCouplingNo_ZI)