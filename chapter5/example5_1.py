# -*- coding=UTF-8 -*-

# 对话框窗体或对话框是现代GUI应用不可或缺的一部分。dialog定义为两个或多个人之间的交谈。
# 在计算机程序中dialog是一个窗体，用来和程序“交谈”。对话框用来输入数据、修改数据、
# 改变程序设置等等。对话框是用户和计算机程序沟通的重要手段。

# QInputDialog 提供一个简单的对话框，以便从用户获取单个值。输入值可以是一个字符串，一个数字或者列表的一项。

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.button = QtGui.QPushButton('Dialog', self)        # 添加按钮
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)           # 将button设置为无法聚焦

        self.button.move(20, 20)
        self.connect(self.button, QtCore.SIGNAL('clicked()'), # 将button的点击信号和自定义的showDialog函数槽连接
                     self.showDialog)
        self.setFocus()

        self.label = QtGui.QLineEdit(self)                      # 添加单行文本框
        self.label.move(130, 22)

        self.setWindowTitle('InputDialog')
        self.setGeometry(300, 300, 350, 80)

    def showDialog(self):
        # 这行代码显示输入对话框，第一个字符串是对话框标题，第二个是对话框里面的消息。
        # 对话框返回输入的文本那一个布尔值。如果我们点击 ok 按钮，布尔值是 True ，否
        # 则为False 。
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
                                              'Enter your name:')
        if ok:
            self.label.setText(str(text))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()