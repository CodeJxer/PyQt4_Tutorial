# -*- coding=UTF-8 -*-

# 颜色对话框为定制颜色提供一个对话框组件。

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 初始颜色为黑色
        color = QtGui.QColor(0, 0, 0)

        # 添加一个按钮
        self.button = QtGui.QPushButton('Dialog', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)

        # 将button的点击信号与showDialog函数槽连接
        self.connect(self.button, QtCore.SIGNAL('clicked()'),
                     self.showDialog)
        self.setFocus()

        # 添加一个面板
        self.widget = QtGui.QWidget(self)
        self.widget.setStyleSheet('QWidget { background-color: %s }'
                                  % color.name())
        self.widget.setGeometry(130, 22, 100, 100)

        self.setWindowTitle('colorDialog')
        self.setGeometry(300, 300, 250, 180)

    def showDialog(self):
        # 这行代码将会弹出一个 QColorDialog 。
        col = QtGui.QColorDialog.getColor()

        # 检查颜色是否有效，如果点击了取消按钮，将返回无效的颜色。如果颜色有效，我们使用样式修改背景颜色。
        if col.isValid():
            self.widget.setStyleSheet('QWidget { background-color: %s }'
                                      % col.name())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()