from mainwindow import *
import sys

from datetime import datetime


fieldsOfInterest = ['dateEdit', 'dateTimeEdit', 'timeEdit', 'horizontalSlider', 'verticalSlider']


def makeLogger(ctx, s):
    def ret():
        b = ctx.radioButton.isChecked()  
        print "has been clicked %s %s" % (s, ctx.txtName.text() )
    return ret

def makeRb(btn, s):
    def ret():
        b = btn.isChecked()  
        print "%s %s" % (b, s)
    return ret

def slider(s, x):
    def ret():
        print s, x.value()
    return ret


def blurb():
    print "Blurb"
    
class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print dir(self.ui)
        print self.ui.pushButton.clicked.connect
        self.ui.pushButton.clicked.connect(   makeLogger(self.ui,   'pushButton1'))
        self.ui.pushButton_2.clicked.connect( makeLogger(self.ui, 'pushButton2'))
        self.ui.txtName.textChanged.connect( makeLogger(self.ui, 'text'))
        
        self.ui.radioButton.clicked.connect( makeRb(self.ui.radioButton, 'radioButton1'))
        self.ui.horizontalSlider.valueChanged.connect( slider('h', self.ui.horizontalSlider ))
        self.ui.verticalSlider.valueChanged.connect( slider('v', self.ui.verticalSlider))
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    #sys.exit(app.exec_())
    app.exec_()

    
    
