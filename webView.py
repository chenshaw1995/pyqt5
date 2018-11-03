
import sys
import requests
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import *
# QWebEngineView
# from PyQt5 import QtWidgets, QtCore, QtGui, QtWebEngineWidgets
# from PyQt5.QtWidgets import *
# from webView import render

def render(source_html, app = None):
    """Fully render HTML, JavaScript and all."""

    class Render(QWebEngineView):
        def __init__(self, url, app = None):
            html = self.getHtml(url)
            self.html = None
            # self.app = app
            QWebEngineView.__init__(self)
            self.loadFinished.connect(self._loadFinished)
            self.setHtml(html)
            # self.show()
            # self.app.exec_()
#             while self.html is None:
#                 self.app.processEvents(QEventLoop.ExcludeUserInputEvents | QEventLoop.ExcludeSocketNotifiers | QEventLoop.WaitForMoreEvents)
#             self.app.quit()   
        def getHtml(self, url):
            return requests.get(url).text

        def refresh(self):
            self.isFirst = True
            self.loadFinished.connect(self.onLoadFinished)

        def onLoadFinished(self, ok):
            if self.isFirst:
                self.sender().Reload()
            self.isFirst = False

        def _callable(self, data):
            self.html = data

        def _loadFinished(self, result):
            self.page().toHtml(self._callable)

#     app = QtWidgets.QApplication([])
# #     webview = QtWebEngineWidgets.QWebEngineView()
# #     webview.setHtml(html)
# #     webview.show()
    return Render(source_html,app)
    

class subWebPage(QWidget):
    """A QWebEngineView is required to display a QWebEnginePage."""

    def __init__(self, parent=None, url=None, html_file=None):
        super().__init__(parent)
        self.view = render(url)
        self.page = QWebEnginePage()

        print("Loading URL:", url)
        self.url = QUrl(url)
        self.page.load(self.url)

        # associate page with view
        self.view.setPage(self.page)

        # set layout
        self.vl = QVBoxLayout()
        self.vl.addWidget(self.view)
        
        # l = QLabel()
        # l.setText("refresh")
        # l.setFrameShape(QFrame.StyledPanel)
        # l.mouseReleaseEvent=lambda event:self.refresh('https://www.microsoft.com')

        # self.vl.addWidget(l)

        self.setLayout(self.vl)
    
    def refresh(self, newUrl):

        self.url = QUrl(newUrl)
        self.page.load(self.url)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    web = subWebPage(url='http://courses.cse.tamu.edu/caverlee/csce670/') 
    web.show()
    sys.exit(app.exec_())

#     test render
#     dummy_url = 'http://courses.cse.tamu.edu/caverlee/csce670/'
#     app = QApplication([])
#     r = render(dummy_url, app)
#     r.show()
#     app.exec_()