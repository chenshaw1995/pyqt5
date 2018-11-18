import sys
import requests
# from menu import Menu
# from urls import URLs
# from inputs import form
# from record import output
# from webView import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Body import *

class StackedExample(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, 'Contact' )
        self.leftlist.insertItem(1, 'Personal' )

        self.central_widget = QWidget()#Body(app)             # define central widget
        self.setCentralWidget(self.central_widget)    # set QMainWindow.centralWidget

        # self.stack1 = Body(app)  #QWidget()
        # self.stack2 = Body(app)  # QWidget()

        # # self.stack1UI()
        # # self.stack2UI()

        # self.Stack = QStackedWidget (self)
        # self.Stack.addWidget (self.stack1)
        # self.Stack.addWidget (self.stack2)
        grid = QGridLayout()
        self.centralWidget().setLayout(grid)          # add the layout to the central widget
        grid.addWidget(self.leftlist,0,0)
        # grid.addWidget(self.Stack,0,1)

        self.leftlist.currentRowChanged.connect(self.display)
        self.resize(300,100)
        self.show()
    
    def display(self):
        pass

if __name__ == '__main__':
    app = QApplication([])
    win = StackedExample()
    win.show()
    sys.exit(app.exec_())