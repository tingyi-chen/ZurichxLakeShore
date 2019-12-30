import sys
from PyQt5.QtWidgets import QApplication
from manager import Manager

app = QApplication(sys.argv)
manager = Manager()
app.exec_()