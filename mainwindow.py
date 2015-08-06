# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Aug  6 02:39:33 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(519, 395)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.radioButton = QtGui.QRadioButton(self.centralWidget)
        self.radioButton.setGeometry(QtCore.QRect(10, 80, 117, 22))
        self.radioButton.setObjectName("radioButton")
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 40, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.txtName = QtGui.QLineEdit(self.centralWidget)
        self.txtName.setGeometry(QtCore.QRect(230, 20, 251, 21))
        self.txtName.setObjectName("txtName")
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.centralWidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(260, 70, 194, 27))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.timeEdit = QtGui.QTimeEdit(self.centralWidget)
        self.timeEdit.setGeometry(QtCore.QRect(260, 110, 118, 27))
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtGui.QDateEdit(self.centralWidget)
        self.dateEdit.setGeometry(QtCore.QRect(260, 160, 111, 27))
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalSlider = QtGui.QSlider(self.centralWidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 190, 160, 29))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalSlider = QtGui.QSlider(self.centralWidget)
        self.verticalSlider.setGeometry(QtCore.QRect(440, 140, 29, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 519, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

