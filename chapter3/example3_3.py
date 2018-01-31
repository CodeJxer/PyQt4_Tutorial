# -*- coding=UTF-8 -*-

# 最常用的布局类是网格布局，网格布局把空间划分成行和列。我们使用 QGridLayout 类来创建网格布局。

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('grid layout')

        names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/',
                '4', '5', '6', '*', '1', '2', '3', '-', '0',
                '.', '=', '+']

        grid = QtGui.QGridLayout()

        j = 0
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
               (1, 0), (1, 1), (1, 2), (1, 3),
               (2, 0), (2, 1), (2, 2), (2, 3),
               (3, 0), (3, 1), (3, 2), (3, 3),
               (4, 0), (4, 1), (4, 2), (4, 3)]

        # 调用addWidget()方法来把窗口组件加到网格中，参数是部件（widget），行（row）和列（column）数字。
        for i in names:
            button = QtGui.QPushButton(i)
            if j == 2:
                grid.addWidget(QtGui.QLabel(''), 0, 2)
            else:
                grid.addWidget(button, pos[j][0], pos[j][1])
            j += 1

        self.setLayout(grid)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())