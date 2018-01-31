# -*- coding=UTF-8 -*-

# 工具栏
import sys
from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('toolbar')

        self.exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        self.exit.setShortcut('Ctrl+Q')
        # 连接"exit"行为的triggered()信号到预定义的close()槽
        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        # 创建一个工具栏并把行为"exit"添加进去
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(self.exit)


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())