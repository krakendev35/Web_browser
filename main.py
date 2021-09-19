from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5 import QtGui
from PyQt5.QtWebEngineWidgets import*


class Kraker():
    def __init__(self):
        
        self.window = QWidget()
        self.window.setWindowTitle("Kraker")
        self.window.setWindowIcon(QtGui.QIcon('logo.png'))

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()
        self.urlBar = QTextEdit()
        self.urlBar.setMaximumHeight(30)

        self.goBtn = QPushButton("Zort")
        self.goBtn.setMinimumHeight(30)
        self.goBtn.setMaximumWidth(60)

        self.forwardBtn = QPushButton(">")
        self.forwardBtn.setMinimumHeight(30)
        self.forwardBtn.setMaximumWidth(60)

        self.backBtn = QPushButton("<")
        self.backBtn.setMinimumHeight(30)
        self.backBtn.setMaximumWidth(60)

        self.horizontal.addWidget(self.urlBar)
        self.horizontal.addWidget(self.goBtn)
        self.horizontal.addWidget(self.backBtn)
        self.horizontal.addWidget(self.forwardBtn)

        
        self.browser = QWebEngineView()

        self.goBtn.clicked.connect(lambda: self.navigate(self.urlBar.toPlainText()))
        self.backBtn.clicked.connect(self.browser.back)
        self.forwardBtn.clicked.connect(self.browser.forward)


        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        
        self.browser.setUrl(QUrl("https://www.google.com"))

        self.window.setLayout(self.layout)
        self.window.show()


    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://"+url
            self.urlBar.setText(url)
        self.browser.setUrl(QUrl(url))
        

app = QApplication([])
window = Kraker()
app.exec_()
