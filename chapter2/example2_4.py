# -*- coding=UTF-8 -*-

#把菜单栏、工具栏和状态栏放在一起

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(350, 250)
        self.setWindowTitle('mainwindow')

        # 这里我们创建了一个文本编辑控件，把它设置成QMainWinow的中心组件。中心组件将会占据所有留下的空间。
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        # 编写"退出"动作
        exit = QtGui.QAction(QtGui.QIcon('icons/guitar.ico'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit)


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())