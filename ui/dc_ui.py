# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VoutSettings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(300, 200))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AdvancedSettings_Vout = QtWidgets.QLabel(self.centralwidget)
        self.AdvancedSettings_Vout.setGeometry(QtCore.QRect(217, 20, 165, 24))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AdvancedSettings_Vout.setFont(font)
        self.AdvancedSettings_Vout.setObjectName("AdvancedSettings_Vout")
        self.DCOffsetRange_Vout = QtWidgets.QLabel(self.centralwidget)
        self.DCOffsetRange_Vout.setGeometry(QtCore.QRect(242, 40, 115, 18))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DCOffsetRange_Vout.setFont(font)
        self.DCOffsetRange_Vout.setObjectName("DCOffsetRange_Vout")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(120, 80, 361, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.VoltageOutGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.VoltageOutGrid.setContentsMargins(0, 0, 0, 0)
        self.VoltageOutGrid.setObjectName("VoltageOutGrid")
        self.VoltageOutLabel1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.VoltageOutLabel1.setObjectName("VoltageOutLabel1")
        self.VoltageOutGrid.addWidget(self.VoltageOutLabel1, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.voltageOutRange = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.voltageOutRange.setObjectName("voltageOutRange")
        self.voltageOutRange.addItem("")
        self.voltageOutRange.addItem("")
        self.voltageOutRange.addItem("")
        self.VoltageOutGrid.addWidget(self.voltageOutRange, 0, 1, 1, 1)
        self.pageUp = QtWidgets.QPushButton(self.centralwidget)
        self.pageUp.setGeometry(QtCore.QRect(20, 10, 61, 32))
        self.pageUp.setObjectName("pageUp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AdvancedSettings_Vout.setText(_translate("MainWindow", "Advanced Settings"))
        self.DCOffsetRange_Vout.setText(_translate("MainWindow", "DC Offset Range"))
        self.VoltageOutLabel1.setText(_translate("MainWindow", "Range"))
        self.voltageOutRange.setItemText(0, _translate("MainWindow", "10"))
        self.voltageOutRange.setItemText(1, _translate("MainWindow", "1"))
        self.voltageOutRange.setItemText(2, _translate("MainWindow", "0.1"))
        self.pageUp.setText(_translate("MainWindow", "＜--"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
