import sys
import pprint
from graph import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from crawlerCall import *
# from mainWindow import * 

crawler_result_file = f'{os.path.dirname(os.path.abspath(__file__) )}/clx/clx/crawl_result.csv'

#  only the form not input
class form(QWidget):
    def __init__(self, app):
        self.app = app
        super(form, self).__init__()
        self.title = 'app init form'
        self.left = 300
        self.top = 300
        self.width = 400
        self.height = 400

        self.fbox = QFormLayout()
        self.inputs = {}

        self.setCol('URL', QLineEdit())
        self.setCol('K', QLineEdit())

        # create validation for url input
        reg_url = QRegExp("(http[s]?://)?[\w]+\.[\w]+\.(com|org|edu|)(\.[\w]+)?/.*")
        input_url_validator = QRegExpValidator(reg_url, self.inputs['URL'])
        self.inputs['URL'].setValidator(input_url_validator)

        reg_k = QRegExp("[0-9]+")
        input_k_validator = QRegExpValidator(reg_k, self.inputs['URL'])
        self.inputs['K'].setValidator(input_k_validator)
        # hbox = QHBoxLayout()
        # hbox.addWidget(QRadioButton("Male"))
        # hbox.addWidget(QRadioButton("Female"))
        # hbox.addStretch()
        # self.setCol("sex",hbox)

        # Create a button in the window
        self.submitBtn = QPushButton('submit')
        # connect button to function submit
        self.submitBtn.clicked.connect(self.submit)

        self.exitBtn   = QPushButton('Exit')
        self.exitBtn.clicked.connect(self.exit)
        self.fbox.addRow(self.submitBtn, self.exitBtn)
        self.setLayout(self.fbox)
        # self.app.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def validate_file(self):
        the_file = crawler_result_file
        if os.path.isfile(the_file) and os.path.getsize(the_file) > 0:
            return True
        else:
            print(f'{the_file} does not exist.')
            return False

    @pyqtSlot()
    def submit(self):
        self.app.body.urls.save_set()

        self.vals = {}        
        for col in self.inputs.keys():
            self.vals[col] = self.inputs[col].text()
            print(f'{col}: "{self.vals[col]}"' )
            self.inputs[col].setText("")
        # TODO multi process, 
        call(url = self.vals['URL'], k = self.vals['K'])    
        # check if file empty
        self.validate_file()
        self.app.body.init_urls(True)
        self.app.graph = graph(self.app, new = True)
        self.exit()
        # self.app.body.appear()
    
    @pyqtSlot()
    def exit(self):
        # sys.exit(0)
        # self.hide() 
        self.close()

    def setCol(self, col_name, input_box):
        self.inputs[col_name] = input_box
        self.fbox.addRow(QLabel(col_name), input_box)

# class App(QMainWindow):
 
#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 textbox - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 400
#         self.height = 140
#         self.initUI()
 
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
 
#         # Create textbox
#         self.textbox = QLineEdit(self)
#         self.textbox.move(20, 20)
#         self.textbox.resize(280,40)
 
#         # Create a button in the window
#         self.button = QPushButton('Show text', self)
#         self.button.move(20,80)
 
#         # connect button to function submit
#         self.button.clicked.connect(self.submit)
#         # self.show()
 
#     @pyqtSlot()
#     def submit(self):
#         textboxValue = self.textbox.text()
#         print(textboxValue)
#         QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
#         self.textbox.setText("")
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = form(app)
    ex.show()
    sys.exit(app.exec_())

# app = QApplication(sys.argv)
# form = Form()
# form.show()
# app.exec_()

# if __name__ == '__main__':
    
#    app = QApplication(sys.argv)
#    win = form()

#    win.show()
#    sys.exit(app.exec_())

# class Form(QDialog):
#     def __init__(self, parent=None):
#         super(Form, self).__init__(parent)

#         self.le = QLineEdit()
#         self.le.setObjectName("host")
#         self.le.setText("Host")

#         self.pb = QPushButton()
#         self.pb.setObjectName("connect")
#         self.pb.setText("Connect") 

#         layout = QFormLayout()
#         layout.addWidget(self.le)
#         layout.addWidget(self.pb)

#         self.setLayout(layout)
#         self.connect(self.pb, SIGNAL("clicked()"),self.buttsubmit)
#         self.setWindowTitle("Learning")

#     def buttsubmit(self):
#         # shost is a QString object
#         shost = self.le.text()
#         print(shost)
