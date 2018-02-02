# -*- coding=UTF-8 -*-

# QFontDialog 是一个用来选择字体的对话框组件。

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        hbox = QtGui.QHBoxLayout()

        button = QtGui.QPushButton('Dialog', self)
        button.setFocusPolicy(QtCore.Qt.NoFocus)
        button.move(20, 20)

        hbox.addWidget(button)

        self.connect(button, QtCore.SIGNAL('clicked()'),
                     self.showDialog)

        self.label = QtGui.QLabel('knowledge only matters', self)
        self.label.move(130, 20)

        # 我们把标签加入到水平框布局中。设置延展因素为1，当我们选择不同的字体时，文字可能变得更大。否则标签可能显示不完全。
        hbox.addWidget(self.label, 1)
        self.setLayout(hbox)

        self.setWindowTitle('FontDialog')
        self.setGeometry(300, 300, 250, 110)

    def showDialog(self):
        # 这里弹出一个字体对话框。
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.label.setFont(font)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()