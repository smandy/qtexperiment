from mainwindow import *
import sys

def makeLogger(ctx, s):
    def ret():
        b = ctx.radioButton.isChecked()  
        print "has been clicked %s %s" % (b, ctx.txtName.text() )
        #print dir(ctx.txtName)
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
        self.ui.radioButton.clicked.connect( makeLogger(self.ui, 'woot'))
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    #sys.exit(app.exec_())
    app.exec_()

    
    
