# -*- coding=UTF-8 -*-

# 切换按钮
# PyQt4没有切换按钮的窗口组件，为了创建切换按钮，我们使用特殊模式的 QPushButton 。
# 切换按钮是指一个两种状态的按钮，按下和非按下。通过点击切换两种状态。在某种状态下
# 来这种方式很合适。

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 初始颜色为黑色
        self.color = QtGui.QColor(0, 0, 0)

        # 添加红色按钮
        self.red = QtGui.QPushButton('Red', self)
        self.red.setCheckable(True)
        self.red.move(10, 10)

        self.connect(self.red, QtCore.SIGNAL('clicked()'),
                     self.setColor)

        # 添加绿色按钮, 并置为可被选中
        self.green = QtGui.QPushButton('Green', self)
        self.green.setCheckable(True)
        self.green.move(10, 60)

        self.connect(self.green, QtCore.SIGNAL('clicked()'),
                     self.setColor)

        # 添加蓝色按钮
        self.blue = QtGui.QPushButton('Blue', self)
        self.blue.setCheckable(True)
        self.blue.move(10, 110)

        self.connect(self.blue, QtCore.SIGNAL('clicked()'),
                     self.setColor)

        # 添加一个正方形区域
        self.square = QtGui.QWidget(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet('QWidget { background-color: %s }'
                                  % self.color.name())

        self.setWindowTitle('ToggleButton')
        self.setGeometry(300, 300, 280, 170)

    def setColor(self):
        # 获取信号来源
        source = self.sender()

        if source.text() == 'Red':      # 红色按钮触发该信号
            if self.red.isChecked():     # 红色按钮当前被选中
                self.color.setRed(255)   # 将颜色的红色通道数值置为255
            else:                        # 红色按钮当前被取消选中
                self.color.setRed(0)     # 将颜色的红色通道数值置为0
        elif source.text() == 'Green':
            if self.green.isChecked():
                self.color.setGreen(255)
            else:
                self.color.setGreen(0)
        else:
            if self.blue.isChecked():
                self.color.setBlue(255)
            else:
                self.color.setBlue(0)

        self.square.setStyleSheet('QWidget { background-color: %s }'
                                  % self.color.name())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
