# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TASettings.ui'
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
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(130, 80, 321, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.ACCoupling = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.ACCoupling.setContentsMargins(0, 0, 0, 0)
        self.ACCoupling.setObjectName("ACCoupling")
        self.ACCouplingLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.ACCouplingLabel.setObjectName("ACCouplingLabel")
        self.ACCoupling.addWidget(self.ACCouplingLabel, 0, QtCore.Qt.AlignHCenter)
        self.ACCouplingValue = QtWidgets.QHBoxLayout()
        self.ACCouplingValue.setObjectName("ACCouplingValue")
        self.acCouplingYes_TA = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.acCouplingYes_TA.setObjectName("acCouplingYes_TA")
        self.ACCouplingValue.addWidget(self.acCouplingYes_TA)
        self.acCouplingNo_TA = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.acCouplingNo_TA.setObjectName("acCouplingNo_TA")
        self.ACCouplingValue.addWidget(self.acCouplingNo_TA)
        self.ACCoupling.addLayout(self.ACCouplingValue)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(130, 130, 321, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.Gain = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.Gain.setContentsMargins(0, 0, 0, 0)
        self.Gain.setObjectName("Gain")
        self.GainLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.GainLabel.setObjectName("GainLabel")
        self.Gain.addWidget(self.GainLabel, 0, QtCore.Qt.AlignHCenter)
        self.gainValue = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.gainValue.setObjectName("gainValue")
        self.gainValue.addItem("")
        self.gainValue.addItem("")
        self.gainValue.addItem("")
        self.gainValue.addItem("")
        self.gainValue.addItem("")
        self.Gain.addWidget(self.gainValue)
        self.gainValue.raise_()
        self.GainLabel.raise_()
        self.AdvancedSettings_TA = QtWidgets.QLabel(self.centralwidget)
        self.AdvancedSettings_TA.setGeometry(QtCore.QRect(217, 20, 165, 24))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AdvancedSettings_TA.setFont(font)
        self.AdvancedSettings_TA.setObjectName("AdvancedSettings_TA")
        self.HF2TA = QtWidgets.QLabel(self.centralwidget)
        self.HF2TA.setGeometry(QtCore.QRect(176, 40, 247, 18))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.HF2TA.setFont(font)
        self.HF2TA.setObjectName("HF2TA")
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
        self.ACCouplingLabel.setText(_translate("MainWindow", "AC Coupling"))
        self.acCouplingYes_TA.setText(_translate("MainWindow", "Yes"))
        self.acCouplingNo_TA.setText(_translate("MainWindow", "No"))
        self.GainLabel.setText(_translate("MainWindow", "Gain"))
        self.gainValue.setItemText(0, _translate("MainWindow", "100"))
        self.gainValue.setItemText(1, _translate("MainWindow", "1000"))
        self.gainValue.setItemText(2, _translate("MainWindow", "10000"))
        self.gainValue.setItemText(3, _translate("MainWindow", "100000"))
        self.gainValue.setItemText(4, _translate("MainWindow", "1000000"))
        self.AdvancedSettings_TA.setText(_translate("MainWindow", "Advanced Settings"))
        self.HF2TA.setText(_translate("MainWindow", "Trans-Impedance Amplifier (HF2TA)"))
        self.pageUp.setText(_translate("MainWindow", "＜--"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
