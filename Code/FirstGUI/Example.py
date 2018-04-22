#!/usr/bin/env python
#_*_coding:utf-8_*_

'''

Author:LipingGen

'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Example")
        self.setWindowIcon(QIcon="..\image\windowIcon.png")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())