from PyQt4.QtCore import  QAbstractTableModel, Qt, QVariant
from PyQt4.QtGui import QApplication, QWidget, QTableView, QVBoxLayout

import sys

my_array = [['00','01','02'],
            ['10','11','12'],
            ['20','21','22']]

def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())

class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        self.tablemodel = MyTableModel(my_array, self)
        self.tableview = QTableView()
        self.tableview.setModel(self.tablemodel)

        layout = QVBoxLayout(self)
        layout.addWidget(self.tableview)
        self.setLayout(layout)

class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])


def main2():
    #app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    #sys.exit(app.exec_())

    
if __name__ == "__main__":
    main2()
