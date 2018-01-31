# -*- coding=UTF-8 -*-

# 菜单栏
import sys
from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('menubar')

        # 编写"退出"动作
        exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.statusBar()

        menubar = self.menuBar()            # 创建一个菜单栏
        file = menubar.addMenu('&File')    # 增加一个名为"File"的菜单项
        file.addAction(exit)                # 为File这个菜单项添加"退出"动作


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
