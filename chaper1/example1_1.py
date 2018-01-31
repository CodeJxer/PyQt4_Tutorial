# -*- coding=UTF-8 -*-

#这个例子十分简单，它仅仅现实一个小窗体。但是我们可以在这个
#窗体上进行很多操作，我们可以调整大小、最大化、最小化。

import sys
from PyQt4 import QtGui                 #基本的GUI组件在QtGui模块中

#每个PyQt4程序必须创建一个application对象
app = QtGui.QApplication(sys.argv)

#QWidget窗口组件是PyQt4中所有用户界面对象的基类
widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('simple')
widget.show()

sys.exit(app.exec_())