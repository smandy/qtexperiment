# -*- coding: utf-8 -*-

try:
    from PySide import QtCore
    from PySide import QtWidgets
except:
    from PyQt4.QtCore import pyqtSlot as Slot
    from PyQt4 import QtCore
    from PyQt4 import QtWidgets

class MyPyClass(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        pass
