import sys
import pprint
from graph import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from crawlerCall import *
# from mainWindow import * 

dirname = os.path.dirname(os.path.abspath(__file__) )
crawler_result_file = os.path.join(dirname, 'clx/clx/crawl_result.csv')

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
        self.submitBtn = QPushButton('submit')
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
    
    @pyqtSlot()
    def exit(self):
        self.close()

    def setCol(self, col_name, input_box):
        self.inputs[col_name] = input_box
        self.fbox.addRow(QLabel(col_name), input_box)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = form(app)
    ex.show()
    sys.exit(app.exec_())
