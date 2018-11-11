import sys
import requests
# from menu import Menu
from urls import URLs
# from inputs import form
from record import output
# from two_url_form import two_url_form
from webView import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Body(QWidget):
    def __init__(self, app):
        super(Body, self).__init__()
        self.app = app
        self.app.title = 'Body-part'
        self.app.body = self
        self.init_size()
        
        # TODO use menu to link the url input form, and url ids input form, 

        #  eliminate inconsistent comparisons, 

        # show topologically sort pages, 

        # show last topological sort result,
        self.url1 = "https://www.google.com"
        self.url2 = "https://www.google.com"

        self.app.body.initUI()
        
        self.init_urls()

        self.app.body.show()

    def init_size(self):
        self.x = 300
        self.y = 300
        self.w = 400
        self.h = 400

    def init_urls(self, update_url = False):
        self.urls = URLs(update_url)
        self.app.k = len(self.urls.list)
        # self.urls.iterator()
        self.update1()
        self.update2()
        
    def update1(self, ids = ""):
        if ids == "":
            self.url1 = self.urls.getNext()
        else:
            self.url1 = self.urls.get_next_by_id(ids)
        self.id1 = self.urls.id
        print(f'url1: "{self.url1}"')
        self.left_page.refresh(self.url1)

    def update2(self, ids = ""):
        if ids == "":
            self.url2 = self.urls.getNext()
        else:
            self.url2 = self.urls.get_next_by_id(ids)
        self.id2 = self.urls.id
        print(f'url2: "{self.url2}"')
        self.right_page.refresh(self.url2)

    def getNewUrl(self, id):
        if id == 1:
            self.update1()
            # self.resize(self.w, self.h)
            # self.left_page.refresh(self.url1)
        else:
            self.update2()
            # self.resize(self.w, self.h)
            # self.right_page.refresh(self.url2)

    def setLeft(self):
        # view = QFrame()
        # view.setFrameShape(QFrame.StyledPanel)
        # view = QLabel('label in a frame')
        # self.left = view

        left_part = QSplitter(Qt.Vertical)
        self.left_page = subWebPage(url=self.url1) 
        left_part.addWidget(self.left_page)
        left_part.addWidget(self.createLabel("choose 1", 1, self.choose))
        self.left = left_part

    def setRight(self):
        # view = QFrame()
        # view.setFrameShape(QFrame.StyledPanel)
        # view = QLabel('label in a frame')
        # self.right = view

        right_part = QSplitter(Qt.Vertical)
        self.right_page = subWebPage(url=self.url2)
        right_part.addWidget(self.right_page)
        right_part.addWidget(self.createLabel("choose 2", 2, self.choose))
        self.right = right_part

    def choose(self, idx):
        r = '%s %s %s' % (self.url1, self.url2, idx)
        
        output(self.app, self.id1, self.id2, idx - 1)
        self.getNewUrl(idx)
        print(r)

    def createLabel(self, txt, idx, f):
        l = QLabel()
        l.setText(txt)
        l.setFrameShape(QFrame.StyledPanel)
        l.mouseReleaseEvent=lambda event:f(idx)
        return l

    def setBottom(self):
         # if False:
        view = QFrame()
        view.setFrameShape(QFrame.StyledPanel)
        view = QLabel('label in a frame')
        # label.show()

        #     self.left = view
        # else:
        # splt = QSplitter(Qt.Horizontal)
        # l1 = self.createLabel("choose 1", 1, self.choose)
        # l2 = self.createLabel("choose 2", 2, self.choose)
        # splt.addWidget(l1)
        # splt.addWidget(l2)
        self.bottom = view#splt 
        # view

    def setTop(self):
        view = QFrame()
        view.setFrameShape(QFrame.StyledPanel)
        view = QLabel('top line')
        self.top = view

        # pass
        # self.menu = Menu()
        # self.top = self.menu
        
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

        # self.body = form

        # update form with splitter1, after inputing info in form, call crawl function, get crawler result, and pass it to urls, 

        self.splitter2.addWidget(self.splitter1)
        # self.splitter2.addWidget(self.body)
        self.splitter2.addWidget(self.bottom)

        hbox.addWidget(self.splitter2)

        self.setLayout(hbox)
        self.app.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setGeometry(self.x, self.y, self.w, self.h)
        self.setWindowTitle(self.app.title)
        # self.show()

def main():
    app = QApplication(sys.argv)
    # ex = form(app)
    ex = Body(app)
    # ex.show()

    

    app.exec_()

    # sys.exit()

if __name__ == '__main__':
    main()