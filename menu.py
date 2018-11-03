import sys
from PyQt5 import QtWidgets


class Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        viewBtn = QtWidgets.QPushButton("File")
        exitAct = QtWidgets.QAction('Exit', self)
        aboutAct = QtWidgets.QAction('About', self)

        toolbar = self.addToolBar("Exit")

        toolbar.addWidget(viewBtn)
        toolbar.addAction(exitAct)
        toolbar.addAction(aboutAct)

        menu = QtWidgets.QMenu()
        menu.addAction("new file")
        menu.addAction("save file")
        menu.addAction("refresh")
        viewBtn.setMenu(menu)

        menu.triggered.connect(lambda action: print(action.text()))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())