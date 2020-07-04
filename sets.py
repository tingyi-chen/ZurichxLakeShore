import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QFormLayout, QSlider, QSpinBox, QSizePolicy, QDoubleSpinBox, QMainWindow
from zurich import Zurich
from PyQt5 import uic
from ui.set_ui import Ui_MainWindow

class Sets(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):          
        super(Sets, self).__init__(parent)

        uic.loadUi("ui/set_ui.ui", self)