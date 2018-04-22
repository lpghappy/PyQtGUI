#!/usr/bin/env python
#_*_coding:utf-8_*_

'''

Author:LipingGen

'''

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import (QIcon, QFont)
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('SansSerif', 10))

        # 创建一个PushButton并为他设置一个tooltip。我们可以使用丰富的文本格式
        btn = QPushButton('退出', self)
        btn.setToolTip("这是一个<b>按钮</b>")
        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())
        # 移动窗口的位置
        btn.move(50, 50)
        # 将按钮连接到信号槽，在单击该按钮时退出窗口
        btn.clicked.connect(QCoreApplication.instance().quit)

        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('Example')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('image/windowIcon.png'))
        # 窗口居中
        self.center()
        # 显示窗口
        self.show()

    # 控制窗口显示在屏幕中心的方法
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 重写closeEvent()事件处理程序
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示框', "您确定退出吗？",
                                     QMessageBox.Yes|QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())