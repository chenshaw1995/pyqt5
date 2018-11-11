import sys
import pprint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from crawlerCall import *

# directly pick two from 1 to k, 

#  only the form not input
class two_url_form(QWidget):
    def __init__(self, app):
        self.app = app
        
        super(two_url_form, self).__init__()
        self.title = 'compare form'
        self.left   = 300
        self.top    = 300
        self.width  = 400
        self.height = 400
        self.fbox   = QFormLayout()
        self.inputs = {}
        self.btns   = {}
        # self.items =[str(x) for x in range(10)]

        self.set_int_col('id1', QLineEdit())
        self.set_int_col('id2', QLineEdit())

        app.sets = set([str(i) for i in range(app.k)])
        # self.app.body.urls.set

        self.compareBtn = QPushButton('compare')
        self.compareBtn.clicked.connect(self.compare)

        self.exitBtn   = QPushButton('Exit')
        self.exitBtn.clicked.connect(self.exit)
        self.fbox.addRow(self.compareBtn, self.exitBtn)
        self.setLayout(self.fbox)

        # QProcess emits `readyRead` when there is data to be read
        # self.process.readyRead.connect(self.dataReady)
        # self.exitBtn.clicked.connect(self.exit)
        # Just to prevent accidentally running multiple times
        # Disable the button when process starts, and enable it when it finishes
        # self.process.started.connect(lambda: self.runButton.setEnabled(False))
        # self.process.finished.connect(lambda: self.runButton.setEnabled(True))
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def set_int_col(self, col_name, input_box):
        self.btns[col_name] = QPushButton(f"Enter an integer for {col_name}")
        self.inputs[col_name] = input_box
        self.fbox.addRow(self.btns[col_name], input_box)
        if col_name == 'id1':
            self.btns['id1'].clicked.connect(self.getint1)
        elif col_name == 'id2':
            self.btns['id2'].clicked.connect(self.getint2)
            
    def getint1(self):
        # item, ok = QInputDialog.getItem(self, "select input dialog", 
        #     "list of languages", self.items, 0, False)
            
        # if ok and item:
        #     self.le.setText(item)
        item, okPressed = QInputDialog.getItem(self, "Get url","url_id:", self.app.sets, 0, False)
        if okPressed and item:
            print(item)
            # self.app.sets.remove(item)
            self.inputs['id1'].setText(str(item))
    
    def getint2(self):
        item, okPressed = QInputDialog.getItem(self, "Get url","url_id:", self.app.sets, 0, False)
        if okPressed and item:
            print(item)
            # self.app.sets.remove(item)
            self.inputs['id2'].setText(str(item))
        # num,ok = QInputDialog.getInt(self,"integer input dualog","enter a number",self.app.k - 1, 0, self.app.k - 1, 1)
        # if ok:
        #     print(num)
        #     self.inputs['id2'].setText(str(num))

    @pyqtSlot()
    def compare(self):
        self.vals = {}
        for col in self.inputs.keys():
            self.vals[col] = self.inputs[col].text()
            print(f'{col}: "{self.vals[col]}"' )
            # self.inputs[col].setText("")
        body = self.app.body
        id1 = self.vals['id1']
        id2 = self.vals['id2']
        if self.app.graph.exist_edge(id1, id2) == True:
            result = self.app.graph.compare(id1, id2)
            message = ""
            if result < 0:
                message = f'{id1} smaller than {id2}'
            elif result > 0:
                message = f'{id2} smaller than {id1}'
            else:
                message = f'{id1} equals to {id2}'
            QMessageBox.about(self, "compare result", message)
        else:
            body.update1(self.vals['id1'])
            body.update2(self.vals['id2'])
        
        # if two urls has been compared, return the result, 
        # if not pop a message so do we need to put these two into body window
        
        # update id1 and id2, if we have a set for all urls, we need to update the set, when leave,
        #  we need to save the set into file. 
        self.exit()
    
    @pyqtSlot()
    def exit(self):
        self.close()
        # self.process.kill
        # self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.k = 10
    app.sets = set([str(i) for i in range(app.k)])
    ex = two_url_form(app)
    ex.show()
    sys.exit(app.exec_())