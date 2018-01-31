# -*- coding=UTF-8 -*-

#应用程序图标是一个小图像，一般显示在标题栏的左上角，
#在接下来的例子中，我们将会展示如何在PyQt中实现。我们
#也会介绍一些新方法。

import sys
from PyQt4 import QtGui

class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)                #设置窗口初始位置以及大小
        self.setWindowTitle('Icon')                        #设置窗口标题
        self.setWindowIcon(QtGui.QIcon('icons/web.png'))


app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())
