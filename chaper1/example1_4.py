# -*- coding=UTF-8 -*-

# 关闭一个窗体很明显的方式是点击标题栏上的x标记，在接下来
# 的例子中，我们将展示如何用编程的方式关闭窗体，我们将简略
# 的接触到信号和槽。

# QPushButton(string text, QWidget parent = None)
# 参数text是显示在按钮上的文本，parent是放置按钮的父亲

import sys
from PyQt4 import QtGui, QtCore


class QuitButton(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')

        # 创建一个按钮并放置在QWidget上，就像把QWidget放置在屏幕上一样。
        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(10, 10, 64, 35)

        # PyQt4中的事件处理系统是建立信号和槽机制。如果点击按钮，信号
        # clicked()将会发射，槽可以是PyQt的槽或者任何的Python调用。
        # QtCore.QObject.connect() 把信号和槽连接起来。在这个例子中槽
        # 是PyQt预定义的quit()槽，发射方和接收方两个对象间进行通讯，发
        # 射方为按钮，接收方为application对象。
        self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))


app = QtGui.QApplication(sys.argv)
qb = QuitButton()
qb.show()
sys.exit(app.exec_())
