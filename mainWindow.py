import sys
import requests
from menu import Menu
from urls import URLs
from record import output
from webView import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class LayOut(QWidget):
    def __init__(self, app):
        super(LayOut, self).__init__()
        self.app = app
        self.x = 300
        self.y = 300
        self.w = 400
        self.h = 400
        self.setUrls()
        # TODO need a input window for url and an integer K, 
        #  then call call function in crawlerCall.py, 
        
        # create a label so user could choose two url by inputing two integer btwn 1 to k, 
        # then show these two pages on screen,  

        # show records btwn two urls by inputing two integer btwn 1 and k,
        #  result would be 1 is bigger than 2, or smaller, or no records,

        #  eliminate inconsistent comparisons, 

        # show topologically sort pages, 

        # show last topological sort result,
        
        self.title = 'mainWindow'
        self.initUI()

    def setUrls(self):
        self.urls = URLs()
        self.urls.iterator()
        self.update1()
        self.update2()
        
    def update1(self):
        self.id1 = self.urls.id
        self.url1 = self.urls.getNext()

    def update2(self):
        self.id2 = self.urls.id
        self.url2 = self.urls.getNext()

    def getNewUrl(self, id):
        if id == 1:
            self.update1()
            # self.resize(self.w, self.h)
            self.left.refresh(self.url1)
        else:
            self.update2()
            # self.resize(self.w, self.h)
            self.right.refresh(self.url2)

    def setLeft(self):
        # if False:
        #     view = QFrame()
        #     view.setFrameShape(QFrame.StyledPanel)
        #     self.left = view
        # else:
        self.left = subWebPage(url=self.url1) 
        # render(requests.get(self.url1).text, self.app)

    def setRight(self):
        self.right = subWebPage(url=self.url2) 

    def choose(self, id):
        r = '%s %s %s' % (self.url1, self.url2, id)# self.url1 + ' ' + self.url2 + " " + id
        numericRecord = '%s %s %s' % (self.id1, self.id2, id - 1)
        output(numericRecord)
        self.getNewUrl(id)
        print(r)

    def createLabel(self, txt, id, f):
        l = QLabel()
        l.setText(txt)
        l.setFrameShape(QFrame.StyledPanel)
        l.mouseReleaseEvent=lambda event:f(id)
        return l

    def setBottom(self):
        splt = QSplitter(Qt.Horizontal)
        l1 = self.createLabel("choose 1", 1, self.choose)
        l2 = self.createLabel("choose 2", 2, self.choose)
        splt.addWidget(l1)
        splt.addWidget(l2)
        self.bottom = splt

    def setTop(self):
        self.menu = Menu()
        self.top = self.menu
        
    def initUI(self):
        hbox = QHBoxLayout(self)
        #  create two widget splited vertically,
        self.setTop()
        self.setLeft()
        self.setRight()
        self.setBottom()

        self.splitter1 = QSplitter(Qt.Horizontal)
        
        self.splitter1.addWidget(self.left)
        self.splitter1.addWidget(self.right)
        self.splitter1.setSizes([200,200])

        self.splitter2 = QSplitter(Qt.Vertical)
        self.splitter2.addWidget(self.top)
        self.splitter2.addWidget(self.splitter1)
        self.splitter2.addWidget(self.bottom)

        hbox.addWidget(self.splitter2)

        self.setLayout(hbox)
        self.app.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setGeometry(self.x, self.y, self.w, self.h)
        self.setWindowTitle(self.title)
        # self.show()

def main():
    app = QApplication(sys.argv)
    
    ex = LayOut(app)
    ex.show()

    app.exec_()

    # sys.exit()

if __name__ == '__main__':
    main()