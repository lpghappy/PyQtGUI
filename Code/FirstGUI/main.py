#!/usr/bin/env python
#_*_coding:utf-8_*_

'''

Author:LipingGen

'''

import sys
import login
from PyQt5.QtWidgets import QApplication, QMainWindow
import time


class UiObject(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ui = login.Ui_MainWindow()
        ui.setupUi(self)

        statusBarMsg = "准备\t\t\t" + time.asctime()
        self.statusBar().showMessage(statusBarMsg)

        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = UiObject()
    sys.exit(app.exec_())
