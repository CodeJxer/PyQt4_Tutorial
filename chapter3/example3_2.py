# -*- coding=UTF-8 -*-

# 使用布局类管理布局更灵活、更实用。这是在窗体上摆放组件的首选方式。基本的布局类是QHBoxLayout和QVBoxLayout，
# 它们可以横向和纵向排列窗口组件。

# 假设我们想要摆放两个按钮到右下角。为了创建这样一个布局，我们需要一个水平框和一个垂直框。我们通过增加延展因素来创建必要的间隔。

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.initUI()

    def initUI(self):
        # 这里我们创建两个按钮。
        okButton = QtGui.QPushButton('OK')
        cancelButton = QtGui.QPushButton('Cancel')

        # 我们创建一个水平框布局，增加一个延展因素和两个按钮。
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 为了创建所需的布局，我们把水平布局放到垂直布局中。
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('box layout')
        self.resize(300, 150)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())