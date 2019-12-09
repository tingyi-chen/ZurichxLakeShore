from home import Home
from sets import Sets
from set_in import SetIn
from set_dc import SetDC
from set_ta import SetTA
from set_demod import SetDemod
from PyQt5.QtWidgets import QApplication
import sys

class Manager():
    def __init__(self):
        self.value = 0
        self.homeWindow()
        
    def homeWindow(self):
        self.home_window = Home()
        self.home_window.show()
        if self.value == 5:
            self.set_window.close()
        self.home_window.advancedSettings.clicked.connect(self.setWindow)
        self.value = 0

    def setWindow(self):
        self.set_window = Sets()
        self.set_window.show()
        if self.value == 0:
            self.home_window.close()
        elif self.value == 1:
            self.ta_window.close()
        elif self.value == 2:
            self.dc_window.close()
        elif self.value == 3:
            self.input_window.close()
        elif self.value == 4:
            self.demod_window.close()
        self.set_window.PageUp.clicked.connect(self.homeWindow)
        self.set_window.TA.clicked.connect(self.taWindow)
        self.set_window.DCOffsetRange.clicked.connect(self.dcWindow)
        self.set_window.VoltageInput.clicked.connect(self.inputWindow)
        self.set_window.Demodulators.clicked.connect(self.demodWindow)
        self.value = 5

    def taWindow(self):
        self.ta_window = SetTA()
        self.ta_window.show()
        self.set_window.close()
        self.ta_window.pageUp.clicked.connect(self.setWindow)
        self.value = 1

    def dcWindow(self):
        self.dc_window = SetDC()
        self.dc_window.show()
        self.set_window.close()
        self.dc_window.pageUp.clicked.connect(self.setWindow)
        self.value = 2

    def inputWindow(self):
        self.input_window = SetIn()
        self.input_window.show()
        self.set_window.close()
        self.input_window.pageUp.clicked.connect(self.setWindow)
        self.value = 3

    def demodWindow(self):
        self.demod_window = SetDemod()
        self.demod_window.show()
        self.set_window.close()
        self.demod_window.pageUp.clicked.connect(self.setWindow)
        self.value = 4

app = QApplication(sys.argv)
manager = Manager()
app.exec_()