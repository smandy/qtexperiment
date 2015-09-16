# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Sep 16 19:41:14 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(619, 468)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.radioButton = QtGui.QRadioButton(self.centralWidget)
        self.radioButton.setGeometry(QtCore.QRect(10, 80, 117, 22))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 0, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 40, 99, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.txtName = QtGui.QLineEdit(self.centralWidget)
        self.txtName.setGeometry(QtCore.QRect(130, 10, 251, 21))
        self.txtName.setObjectName(_fromUtf8("txtName"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.centralWidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(130, 40, 194, 27))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.timeEdit = QtGui.QTimeEdit(self.centralWidget)
        self.timeEdit.setGeometry(QtCore.QRect(130, 70, 118, 27))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.dateEdit = QtGui.QDateEdit(self.centralWidget)
        self.dateEdit.setGeometry(QtCore.QRect(130, 100, 111, 27))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalSlider = QtGui.QSlider(self.centralWidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 130, 160, 29))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.verticalSlider = QtGui.QSlider(self.centralWidget)
        self.verticalSlider.setGeometry(QtCore.QRect(390, 10, 29, 160))
        self.verticalSlider.setProperty("value", 23)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.tableView = QtGui.QTableView(self.centralWidget)
        self.tableView.setGeometry(QtCore.QRect(10, 210, 601, 211))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.progressbar = QtGui.QProgressBar(self.centralWidget)
        self.progressbar.setGeometry(QtCore.QRect(40, 180, 481, 23))
        self.progressbar.setProperty("value", 75)
        self.progressbar.setObjectName(_fromUtf8("progressbar"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 619, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.radioButton.setText(_translate("MainWindow", "RadioButton", None))
        self.pushButton.setText(_translate("MainWindow", "ADD", None))
        self.pushButton_2.setText(_translate("MainWindow", "DELETE", None))

