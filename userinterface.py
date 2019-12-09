# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 484)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SweeperSettingsTab = QtWidgets.QWidget(self.centralwidget)
        self.SweeperSettingsTab.setEnabled(True)
        self.SweeperSettingsTab.setObjectName("SweeperSettingsTab")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.SweeperSettingsTab)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(130, 370, 386, 61))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_6)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tdafConfirm = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.tdafConfirm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tdafConfirm.setObjectName("tdafConfirm")
        self.horizontalLayout_2.addWidget(self.tdafConfirm)
        self.tdafStart = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.tdafStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tdafStart.setObjectName("tdafStart")
        self.horizontalLayout_2.addWidget(self.tdafStart)
        self.tdafCancel = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.tdafCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tdafCancel.setObjectName("tdafCancel")
        self.horizontalLayout_2.addWidget(self.tdafCancel)
        self.tdafDeviceNameInput = QtWidgets.QLineEdit(self.SweeperSettingsTab)
        self.tdafDeviceNameInput.setGeometry(QtCore.QRect(110, 90, 291, 31))
        self.tdafDeviceNameInput.setObjectName("tdafDeviceNameInput")
        self.splitter = QtWidgets.QSplitter(self.SweeperSettingsTab)
        self.splitter.setGeometry(QtCore.QRect(23, 83, 77, 251))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.TDAFLabel1 = QtWidgets.QLabel(self.splitter)
        self.TDAFLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.TDAFLabel1.setObjectName("TDAFLabel1")
        self.TDAFLabel4 = QtWidgets.QLabel(self.splitter)
        self.TDAFLabel4.setAlignment(QtCore.Qt.AlignCenter)
        self.TDAFLabel4.setObjectName("TDAFLabel4")
        self.TDAFLabel7 = QtWidgets.QLabel(self.splitter)
        self.TDAFLabel7.setAlignment(QtCore.Qt.AlignCenter)
        self.TDAFLabel7.setObjectName("TDAFLabel7")
        self.TDAFLabel10 = QtWidgets.QLabel(self.splitter)
        self.TDAFLabel10.setAlignment(QtCore.Qt.AlignCenter)
        self.TDAFLabel10.setObjectName("TDAFLabel10")
        self.splitter_2 = QtWidgets.QSplitter(self.SweeperSettingsTab)
        self.splitter_2.setGeometry(QtCore.QRect(100, 130, 101, 201))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.tdafTStartValue = QtWidgets.QDoubleSpinBox(self.splitter_2)
        self.tdafTStartValue.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tdafTStartValue.setFont(font)
        self.tdafTStartValue.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tdafTStartValue.setMouseTracking(False)
        self.tdafTStartValue.setAccessibleName("")
        self.tdafTStartValue.setAutoFillBackground(False)
        self.tdafTStartValue.setStyleSheet("")
        self.tdafTStartValue.setWrapping(False)
        self.tdafTStartValue.setFrame(True)
        self.tdafTStartValue.setAlignment(QtCore.Qt.AlignCenter)
        self.tdafTStartValue.setProperty("showGroupSeparator", False)
        self.tdafTStartValue.setObjectName("tdafTStartValue")
        self.tdafDCStartValue = QtWidgets.QDoubleSpinBox(self.splitter_2)
        self.tdafDCStartValue.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tdafDCStartValue.setAlignment(QtCore.Qt.AlignCenter)
        self.tdafDCStartValue.setObjectName("tdafDCStartValue")
        self.tdafACStartValue = QtWidgets.QDoubleSpinBox(self.splitter_2)
        self.tdafACStartValue.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tdafACStartValue.setAlignment(QtCore.Qt.AlignCenter)
        self.tdafACStartValue.setObjectName("tdafACStartValue")
        self.tdafFStartValue = QtWidgets.QSpinBox(self.splitter_2)
        self.tdafFStartValue.setMinimumSize(QtCore.QSize(101, 0))
        self.tdafFStartValue.setMaximumSize(QtCore.QSize(101, 16777215))
        self.tdafFStartValue.setAlignment(QtCore.Qt.AlignCenter)
        self.tdafFStartValue.setReadOnly(False)
        self.tdafFStartValue.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.tdafFStartValue.setObjectName("tdafFStartValue")
        self.splitter_3 = QtWidgets.QSplitter(self.SweeperSettingsTab)
        self.splitter_3.setGeometry(QtCore.QRect(240, 130, 51, 201))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.TDAFLabel2 = QtWidgets.QLabel(self.splitter_3)
        self.TDAFLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.TDAFLabel2.setObjectName("TDAFLabel2")
        self.TDAFLabel5 = QtWidgets.QLabel(self.splitter_3)
        self.TDAFLabel5.setAlignment(QtCore.Qt.AlignCenter)
        self.TDAFLabel5.setObjectName("TDAFLabel5")
        self.TDAFLabel8 = QtWidgets.QLabel(self.splitter_3)
        self.TDAFLabel8.setAlignment(QtCore.Qt.AlignCenter)
        self.TDAFLabel8.setObjectName("TDAFLabel8")
        self.TDAFLabel11 = QtWidgets.QLabel(self.splitter_3)
        self.TDAFLabel11.setAlignment(QtCore.Qt.AlignCenter)
        self.TDAFLabel11.setObjectName("TDAFLabel11")
        self.splitter_4 = QtWidgets.QSplitter(self.SweeperSettingsTab)
        self.splitter_4.setGeometry(QtCore.QRect(300, 130, 101, 201))
        self.splitter_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.splitter_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.splitter_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setOpaqueResize(True)
        self.splitter_4.setChildrenCollapsible(True)
        self.splitter_4.setObjectName("splitter_4")
        self.tdafTStopValue = QtWidgets.QDoubleSpinBox(self.splitter_4)
        self.tdafTStopValue.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tdafTStopValue.setAlignment(QtCore.Qt.AlignCenter)
        self.tdafTStopValue.setProperty("showGroupSeparator", False)
        self.tdafTStopValue.setObjectName("tdafTStopValue")
        self.tdafDCStopValue = QtWidgets.QDoubleSpinBox(self.splitter_4)
        self.tdafDCStopValue.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tdafDCStopValue.setAlignment(QtCore.Qt.AlignCenter)
        self.tdafDCStopValue.setObjectName("tdafDCStopValue")
        self.tdafACStopValue = QtWidgets.QDoubleSpinBox(self.splitter_4)
        self.tdafACStopValue.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tdafACStopValue.setAlignment(QtCore.Qt.AlignCenter)
        self.tdafACStopValue.setObjectName("tdafACStopValue")
        self.tdafFStopValue = QtWidgets.QSpinBox(self.splitter_4)
        self.tdafFStopValue.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tdafFStopValue.setAlignment(QtCore.Qt.AlignCenter)
        self.tdafFStopValue.setObjectName("tdafFStopValue")
        self.splitter_6 = QtWidgets.QSplitter(self.SweeperSettingsTab)
        self.splitter_6.setGeometry(QtCore.QRect(520, 80, 101, 251))
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.TDAFTcurrentDisplay = QtWidgets.QDoubleSpinBox(self.splitter_6)
        self.TDAFTcurrentDisplay.setEnabled(True)
        self.TDAFTcurrentDisplay.setFocusPolicy(QtCore.Qt.NoFocus)
        self.TDAFTcurrentDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.TDAFTcurrentDisplay.setReadOnly(True)
        self.TDAFTcurrentDisplay.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.TDAFTcurrentDisplay.setObjectName("TDAFTcurrentDisplay")
        self.tdafTStepValue = QtWidgets.QDoubleSpinBox(self.splitter_6)
        self.tdafTStepValue.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tdafTStepValue.setAlignment(QtCore.Qt.AlignCenter)
        self.tdafTStepValue.setObjectName("tdafTStepValue")
        self.tdafDCStepValue = QtWidgets.QDoubleSpinBox(self.splitter_6)
        self.tdafDCStepValue.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tdafDCStepValue.setAlignment(QtCore.Qt.AlignCenter)
        self.tdafDCStepValue.setObjectName("tdafDCStepValue")
        self.tdafACStepValue = QtWidgets.QDoubleSpinBox(self.splitter_6)
        self.tdafACStepValue.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tdafACStepValue.setAlignment(QtCore.Qt.AlignCenter)
        self.tdafACStepValue.setObjectName("tdafACStepValue")
        self.tdafFSampleCountValue = QtWidgets.QSpinBox(self.splitter_6)
        self.tdafFSampleCountValue.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tdafFSampleCountValue.setAlignment(QtCore.Qt.AlignCenter)
        self.tdafFSampleCountValue.setObjectName("tdafFSampleCountValue")
        self.splitter_5 = QtWidgets.QSplitter(self.SweeperSettingsTab)
        self.splitter_5.setGeometry(QtCore.QRect(430, 80, 82, 251))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.TDAFLabel13 = QtWidgets.QLabel(self.splitter_5)
        self.TDAFLabel13.setAlignment(QtCore.Qt.AlignCenter)
        self.TDAFLabel13.setObjectName("TDAFLabel13")
        self.TDAFLabel3 = QtWidgets.QLabel(self.splitter_5)
        self.TDAFLabel3.setAlignment(QtCore.Qt.AlignCenter)
        self.TDAFLabel3.setObjectName("TDAFLabel3")
        self.TDAFLabel6 = QtWidgets.QLabel(self.splitter_5)
        self.TDAFLabel6.setAlignment(QtCore.Qt.AlignCenter)
        self.TDAFLabel6.setObjectName("TDAFLabel6")
        self.TDAFLabel9 = QtWidgets.QLabel(self.splitter_5)
        self.TDAFLabel9.setAlignment(QtCore.Qt.AlignCenter)
        self.TDAFLabel9.setObjectName("TDAFLabel9")
        self.TDAFLabel12 = QtWidgets.QLabel(self.splitter_5)
        self.TDAFLabel12.setAlignment(QtCore.Qt.AlignCenter)
        self.TDAFLabel12.setObjectName("TDAFLabel12")
        self.advancedSettings = QtWidgets.QToolButton(self.SweeperSettingsTab)
        self.advancedSettings.setGeometry(QtCore.QRect(610, 10, 31, 22))
        self.advancedSettings.setObjectName("advancedSettings")
        self.label_2 = QtWidgets.QLabel(self.SweeperSettingsTab)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.SweeperSettingsTab)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 22))
        self.menubar.setObjectName("menubar")
        self.menuZurich_Instruments_Control_Panel = QtWidgets.QMenu(self.menubar)
        self.menuZurich_Instruments_Control_Panel.setObjectName("menuZurich_Instruments_Control_Panel")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout_PyZurich = QtWidgets.QAction(MainWindow)
        self.actionAbout_PyZurich.setObjectName("actionAbout_PyZurich")
        self.menuZurich_Instruments_Control_Panel.addAction(self.actionAbout_PyZurich)
        self.menubar.addAction(self.menuZurich_Instruments_Control_Panel.menuAction())
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tdafConfirm.setText(_translate("MainWindow", "Confirm"))
        self.tdafStart.setText(_translate("MainWindow", "Start"))
        self.tdafCancel.setText(_translate("MainWindow", "Cancel"))
        self.label.setText(_translate("MainWindow", "DeviceName"))
        self.TDAFLabel1.setText(_translate("MainWindow", "T Start"))
        self.TDAFLabel4.setText(_translate("MainWindow", "DC Start"))
        self.TDAFLabel7.setText(_translate("MainWindow", "AC Start"))
        self.TDAFLabel10.setText(_translate("MainWindow", "F Start"))
        self.tdafTStartValue.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>T Start</p></body></html>"))
        self.TDAFLabel2.setText(_translate("MainWindow", "T Stop"))
        self.TDAFLabel5.setText(_translate("MainWindow", "DC Stop"))
        self.TDAFLabel8.setText(_translate("MainWindow", "AC Stop"))
        self.TDAFLabel11.setText(_translate("MainWindow", "F Stop"))
        self.TDAFLabel13.setText(_translate("MainWindow", "T current"))
        self.TDAFLabel3.setText(_translate("MainWindow", "T Step"))
        self.TDAFLabel6.setText(_translate("MainWindow", "DC Step"))
        self.TDAFLabel9.setText(_translate("MainWindow", "AC Step"))
        self.TDAFLabel12.setText(_translate("MainWindow", "SampleCount"))
        self.advancedSettings.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Temperaure / DC / AC / Frequency Sweep Mode"))
        self.menuZurich_Instruments_Control_Panel.setTitle(_translate("MainWindow", "PyZurich"))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionAbout_PyZurich.setText(_translate("MainWindow", "About PyZurich"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())