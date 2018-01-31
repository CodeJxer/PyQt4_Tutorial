# -*- coding=UTF-8 -*-

# 下面的脚本我们将展示如何在屏幕中央显示窗体。

import sys
from PyQt4 import QtGui


class Center(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle('center')
        self.resize(800, 550)
        self.center()

    def center(self):
        # 计算屏幕分辨率
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

app = QtGui.QApplication(sys.argv)
qb = Center()
qb.show()
sys.exit(app.exec_())
