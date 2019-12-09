import sys
from PyQt5.QtWidgets import QMainWindow
from zurich import Zurich
from PyQt5 import uic
from ui.home_ui import Ui_MainWindow

class Home(QMainWindow, Ui_MainWindow):
    '''1.  定義出 MyWidget 這個新的 class，繼承自外觀空白一片的 QWidget，好讓我們自行塞入東西。
        內含兩個 memfunc：建構式 __init__() 和自行設計的函式 createLayout()。
    2.  定義建構式。因為我們的 class 不需要寄生在其它 widget 中，所以設定參數 parent = None，以成為 top-level window。
    3.  讓 MyWidget 的建構式調用 parent class 的建構式。這個過程是必備的，因為繼承得來的 __init__() 已被覆寫，
        Python 不會再自動調用 parent class 的建構式；QWidget 未被初始化的話，MyWidget 一開就會瞬間爆炸。
    4.  super() 這樣的語法，讓 Python 能自動判別 MyWidget 的 parent class，避免直接寫死在程式碼內。
    5.  連結語法範例
        (1) .connect(method/function)
        (2) self.spinBox.valueChanged.connect(self.setvac)
    6.  functool.partial() makes one can combine 1 function with several parameters into 1 input.
    '''

    def __init__(self, parent = None):          
        super(Home, self).__init__(parent)
        self.zurich = Zurich('dev1521', 0)
        uic.loadUi("ui/home_ui.ui", self)
        self.setTDAFSweep()

    def setTDAFSweep(self):
        self.Start.setEnabled(False)

        self.deviceName.setText('Default')
        self.deviceName.textChanged.connect(self.zurich.setDeviceName)

        self.fStartValue.setRange(0, 10e8)
        self.fStopValue.setRange(0, 10e8)
        self.fStartValue.setValue(100)
        self.fStopValue.setValue(10000)
        self.fSampleCountValue.setRange(0, 301)
        self.fStartValue.valueChanged.connect(self.zurich.setFreqMin)
        self.fStopValue.valueChanged.connect(self.zurich.setFreqMax)
        self.fSampleCountValue.valueChanged.connect(self.zurich.setSamplecount)
        self.fSampleCountValue.setValue(21)

        self.dcStartValue.setSingleStep(0.1)
        self.dcStopValue.setSingleStep(0.1)
        self.dcStepValue.setSingleStep(0.1)
        self.dcStartValue.setRange(-1, 1)
        self.dcStopValue.setRange(-1, 1)
        self.dcStepValue.setRange(-1, 1)
        self.dcStartValue.setValue(0.1)
        self.dcStopValue.setValue(0.2)
        self.dcStepValue.setValue(0.1)
        
        self.dcStartValue.valueChanged.connect(self.zurich.setVdcMin)
        self.dcStopValue.valueChanged.connect(self.zurich.setVdcMax)
        self.dcStepValue.valueChanged.connect(self.zurich.setVdcStep)

        self.acStartValue.setSingleStep(0.1)
        self.acStopValue.setSingleStep(0.1)
        self.acStepValue.setSingleStep(0.1)
        self.acStartValue.setRange(-1, 1)
        self.acStopValue.setRange(-1, 1)
        self.acStepValue.setRange(-1, 1)
        self.acStartValue.setValue(0.1)
        self.acStopValue.setValue(0.4)
        self.acStepValue.setValue(0.1)

        self.acStartValue.valueChanged.connect(self.zurich.setVacMin)
        self.acStopValue.valueChanged.connect(self.zurich.setVacMax)
        self.acStepValue.valueChanged.connect(self.zurich.setVacStep)

        self.tempStartValue.setRange(0, 2000)
        self.tempStopValue.setRange(0,2000)
        self.tempStepValue.setRange(0, 50)
        self.tempStartValue.setSingleStep(5)
        self.tempStopValue.setSingleStep(5)
        self.tempStepValue.setSingleStep(5)
        self.tempStartValue.setValue(300)
        self.tempStopValue.setValue(310)
        self.tempStepValue.setValue(10)
        self.tempStartValue.valueChanged.connect(self.zurich.setTempMin)
        self.tempStopValue.valueChanged.connect(self.zurich.setTempMax)
        self.tempStepValue.valueChanged.connect(self.zurich.setTempStep)

        self.Confirm.clicked.connect(self.setInputDisabled)
        self.Start.clicked.connect(self.zurich.Start)
        self.Cancel.clicked.connect(self.cancel)

    def cancel(self):
        self.zurich.sigoutsOff()
        exit()

    def setInputDisabled(self):
        self.Confirm.setEnabled(False)
        self.Start.setEnabled(True)
        self.deviceName.setEnabled(False)
        self.fStartValue.setEnabled(False)
        self.fStopValue.setEnabled(False)
        self.fSampleCountValue.setEnabled(False)

        self.dcStartValue.setEnabled(False)
        self.dcStopValue.setEnabled(False)
        self.dcStepValue.setEnabled(False)
    
        self.acStartValue.setEnabled(False)
        self.acStopValue.setEnabled(False)
        self.acStepValue.setEnabled(False)

        self.tempStartValue.setEnabled(False)
        self.tempStopValue.setEnabled(False)
        self.tempStepValue.setEnabled(False)