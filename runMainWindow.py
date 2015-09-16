from PyQt4.QtCore import  QAbstractTableModel, Qt, QVariant, QModelIndex
from PyQt4 import QtGui
import mainWindow as mw
import sys
import random

class Foo:
    def __init__(self):
        self.x = random.randint(5,10)

class FooDelegate(QtGui.QStyledItemDelegate):
    def __init__(self):
        QtGui.QStyledItemDelegate.__init__(self)
        self.progressBar = QtGui.QStyleOptionProgressBarV2()
        self.multiplier = 1.0
    
    def paint(self, painter, option, index):
        item = index.data()
        #print item, index.column(), item.toPyObject()
        progressBar = self.progressBar
        #progressBar = item.toPyObject()
        #print progressBar
        progressBar.state = QtGui.QStyle.State_Enabled
        progressBar.direction = QtGui.QApplication.layoutDirection()
        progressBar.rect = option.rect
        progressBar.fontMetrics = QtGui.QApplication.fontMetrics()
        progressBar.minimum = 0
        progressBar.maximum = 100
        progressBar.textAlignment = Qt.AlignCenter
        d = item.toPyObject()
        #print 'd', d, type(d)
        progressBar.progress = int(d * self.multiplier)  # for testing
        QtGui.QApplication.style().drawControl(QtGui.QStyle.CE_ProgressBar, progressBar, painter)
        #return super(FooDelegate, self).paint(painter, option, index)
        
my_array = [['00','01','02', 20],
            ['10','11','12', 30],
            ['20','21','22', 40] ]

fooDelegate = FooDelegate()

fieldsOfInterest = ['dateEdit',
                    'dateTimeEdit',
                    'timeEdit',
                    'horizontalSlider',
                    'verticalSlider']

def makeLogger(ctx, s):
    def ret():
        b = ctx.radioButton.isChecked()  
        print "has been clicked %s %s %s" % (s, ctx.txtName.text(), b )
    return ret

def makeRb(btn, s):
    def ret():
        b = btn.isChecked()  
        print "%s %s" % (b, s)
    return ret

def slider(s, x, target = None):
    def ret():
        #print s, x.value()
        if target:
            target.setValue(x.value())
            fooDelegate.multiplier = x.value() / 100.0
    return ret

def slider2(s, x, target = None):
    def ret():
        #print s, x.value()
        if target:
            target.setValue(x.value())
            fooDelegate.multiplier = x.value() / 100.0
            w.tablemodel.fireChange()
            #print "Boom"
    return ret

def blurb():
    print "Blurb"

class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain

    def fireChange(self):
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))

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
    
    
class ControlMainWindow(QtGui.QMainWindow):
    def addRow(self):
        print "Addrow has been called"
        self.tablemodel.beginInsertRows(QModelIndex(), 0,0)
        self.tablemodel.arraydata.insert( 0, ['10','11','12', random.randint(50,70)] )
        self.tablemodel.endInsertRows()

    def removeRow(self):
        print "RemoveRow  has been called"
        ad = self.tablemodel.arraydata
        lad = len(ad)
        self.tablemodel.beginRemoveRows(QModelIndex(), lad-1,lad-1)
        ad.pop( lad-1)
        self.tablemodel.endRemoveRows()

        
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = mw.Ui_MainWindow()
        self.ui.setupUi(self)
        print dir(self.ui)
        print self.ui.pushButton.clicked.connect
        self.ui.pushButton.clicked.connect(   makeLogger(self.ui,   'pushButton1'))
        self.ui.pushButton.clicked.connect( self.addRow)
        self.ui.pushButton_2.clicked.connect( makeLogger(self.ui, 'pushButton2'))
        self.ui.pushButton_2.clicked.connect( self.removeRow)

        self.ui.txtName.textChanged.connect( makeLogger(self.ui, 'text'))
        self.ui.radioButton.clicked.connect( makeRb(self.ui.radioButton, 'radioButton1'))
        self.ui.horizontalSlider.valueChanged.connect( slider2('h',
                                                              self.ui.horizontalSlider,
                                                              self.ui.progressbar))

        
        self.ui.verticalSlider.valueChanged.connect( slider('v', self.ui.verticalSlider, self.ui.horizontalSlider))


        self.tablemodel = MyTableModel(my_array, self)
        self.ui.tableView.setItemDelegateForColumn(3, fooDelegate)
        self.ui.tableView.setModel(self.tablemodel)
        #self.ui.horizontalSlider.valueChanged.connect( self.tablemodel.dataChanged)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    app.exec_()

w = ControlMainWindow()
w.show()
    
    
    
#tv = 
