# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 70, 271, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.DCOffsetRange = QtWidgets.QPushButton(self.layoutWidget)
        self.DCOffsetRange.setObjectName("DCOffsetRange")
        self.gridLayout.addWidget(self.DCOffsetRange, 0, 0, 1, 1)
        self.VoltageInput = QtWidgets.QPushButton(self.layoutWidget)
        self.VoltageInput.setObjectName("VoltageInput")
        self.gridLayout.addWidget(self.VoltageInput, 1, 0, 1, 1)
        self.Demodulators = QtWidgets.QPushButton(self.layoutWidget)
        self.Demodulators.setObjectName("Demodulators")
        self.gridLayout.addWidget(self.Demodulators, 2, 0, 1, 1)
        self.TA = QtWidgets.QPushButton(self.layoutWidget)
        self.TA.setObjectName("TA")
        self.gridLayout.addWidget(self.TA, 3, 0, 1, 1)
        self.PageUp = QtWidgets.QPushButton(self.centralwidget)
        self.PageUp.setGeometry(QtCore.QRect(20, 10, 61, 32))
        self.PageUp.setObjectName("PageUp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Advanced Settings"))
        self.DCOffsetRange.setText(_translate("MainWindow", "Voltage Output"))
        self.VoltageInput.setText(_translate("MainWindow", "Voltage Input"))
        self.Demodulators.setText(_translate("MainWindow", "Demodulators"))
        self.TA.setText(_translate("MainWindow", "Trans-Impedance Amplifier (HF2TA)"))
        self.PageUp.setText(_translate("MainWindow", "<--"))
