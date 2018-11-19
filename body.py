import sys
import os
import requests
from pathlib import Path
from urls import URLs
from record import output
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
        if update_url:
            self.urls = URLs(update_url = True)
        else:
            crawler_res = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'clx\\clx\\crawl_result.csv')
            if not os.path.isfile(crawler_res):
                Path(crawler_res).touch()

            self.urls = URLs()
        self.app.k = len(self.urls.list)
        
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
        else:
            self.update2()

    def setLeft(self):
        left_part = QSplitter(Qt.Vertical)
        self.left_page = subWebPage(url=self.url1) 
        left_part.addWidget(self.left_page)
        left_part.addWidget(self.createLabel("choose 1", 1, self.choose))
        self.left = left_part

    def setRight(self):
        right_part = QSplitter(Qt.Vertical)
        self.right_page = subWebPage(url=self.url2)
        right_part.addWidget(self.right_page)
        right_part.addWidget(self.createLabel("choose 2", 2, self.choose))
        self.right = right_part

    def choose(self, idx):
        r = '%s %s %s' % (self.url1, self.url2, idx)
        # case, two url are the same
        if self.url1 == self.url2:
            if len(self.urls.list) <= 1:
                # pop_message("")
                QMessageBox.about(self, "error reminder", "only one url left here, please update urls or close current program.")

            self.getNewUrl(idx)
            pass
        else:
            
            output(self.app, self.id1, self.id2, idx - 1)
            if idx - 1 == 0:
                print(f'choose{self.id1}')
                self.urls.remove_from_id(str(self.id1))
            else:
                print(f'choose{self.id2}')
                self.urls.remove_from_id(str(self.id2))

            self.getNewUrl(idx)
            print(r)

    def createLabel(self, txt, idx, f):
        l = QLabel()
        l.setText(txt)
        l.setFrameShape(QFrame.StyledPanel)
        l.mouseReleaseEvent=lambda event:f(idx)
        return l

    def create_empty_view(self):
        view = QFrame()
        view.setFrameShape(QFrame.StyledPanel)
        view = QLabel('label in a frame')
        return view

    def setBottom(self):
        self.bottom = self.create_empty_view()

    def setTop(self):
        view = QFrame()
        view.setFrameShape(QFrame.StyledPanel)
        view = QLabel('top line')
        self.top = view
        
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
        self.setWindowTitle(self.app.title)
        # self.show()

def main():
    app = QApplication(sys.argv)
    ex = Body(app)
    app.exec_()

if __name__ == '__main__':
    main()