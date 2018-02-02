# -*- coding=UTF-8 -*-

# 有时需要方便的知道哪个组件发出的信号，PyQt4有 sender() 方法。

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 添加两个按钮
        button1 = QtGui.QPushButton('Button 1', self)
        button1.move(30, 50)

        button2 = QtGui.QPushButton('Button 2', self)
        button2.move(150, 50)

        # 将两个按钮的点击事件连接到函数buttonClicked()上
        self.connect(button1, QtCore.SIGNAL('clicked()'),
                     self.buttonClicked)

        self.connect(button2, QtCore.SIGNAL('clicked()'),
                     self.buttonClicked)

        self.statusBar().showMessage('Ready')
        self.setWindowTitle('Event sender')
        self.resize(300, 150)

    def buttonClicked(self):
        # 调用这个函数的信号
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())