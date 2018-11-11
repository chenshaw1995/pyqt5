import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from body import *
from urls import URLs
from inputs import form
from record import output
from two_url_form import two_url_form
new_url = 'new_url'
pick_two_urls = "choose two urls"

class Menu(QtWidgets.QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.init_top_menu()
        
        self.input_new_url_form()
        # TODO need to connect to new url btn, 

        self.input_two_urls_form()
        # TODO need slightly modify on compare func, to return the compare result and not use set
        # the result : show records btwn two urls by inputing two integer btwn 1 and k,
        #  result would be 1 is bigger than 2, or smaller, or no records,

        
        # self.compare_two_urls_form()

        self.app.body = Body(app)

        self.setCentralWidget(app.body)

    # def compare_two_urls_form(self):
    #     self.compare_two_urls_form = compare_two_urls_form

    def init_top_menu(self):
        viewBtn = QtWidgets.QPushButton("urls")
        exitAct = QtWidgets.QAction('Exit', self)
        aboutAct = QtWidgets.QAction('About', self)
        
        toolbar = self.addToolBar("Exit")

        toolbar.addWidget(viewBtn)
        toolbar.addAction(exitAct)
        toolbar.addAction(aboutAct)

        menu = QtWidgets.QMenu()
        menu.addAction(new_url)
        menu.addAction(pick_two_urls)
        menu.addAction("compare two urls")
        viewBtn.setMenu(menu)

        exitAct.triggered.connect(self.close)
        aboutAct.triggered.connect(self.introduce_me)
        menu.triggered.connect(lambda action: self.p(action) )

    def input_two_urls_form(self):
        self.app.two_url_form = two_url_form(self.app)

    def input_new_url_form(self):
        self.app.new_url_form = form(self.app)


    def introduce_me(self):
        print("event introduce")
        # reply = QMessageBox.question(self, 'Message',
        #     "about me", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        # if reply == QtGui.QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()

    def p(self, action):
        act = action.text()
        print(act)
        if act == new_url:
            self.app.new_url_form.show()
            
            pass
        elif act == pick_two_urls:
            self.app.two_url_form.show()
            pass
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    menu = Menu(app)
    menu.show()
    sys.exit(app.exec_())