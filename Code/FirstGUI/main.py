#!/usr/bin/env python
#_*_coding:utf-8_*_

'''

Author:LipingGen

'''

import sys
import login
from PyQt5.QtWidgets import QApplication, QMainWindow

class UiObject(object):
    def initUI(self):
        app = self.QApplication(sys.argv)
        MainWindow = self.QMainWindow()
        ui = login.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())



if __name__ == "__main__":
    app = UiObject
    app.initUI()