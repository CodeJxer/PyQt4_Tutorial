# -*- coding=UTF-8 -*-

# QFileDialog允许用户选择文件或文件夹，可选择文件来打开和保存。

import sys
from PyQt4 import QtGui, QtCore

# 这个例子建立在 QMainWindow 组件上，因为我们需要在中间设置文本编辑器。
class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.setFocus()

        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        self.connect(openFile, QtCore.SIGNAL('triggered()'),
                     self.showDialog)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('OpenFile')

    def showDialog(self):
        # 我们弹出 QFileDialog ， getOpenFileName 方法的
        # 第一个字符串是标题，
        # 第二个字符串指定对话框的工作目录，
        # 文件过滤默认设置 All files(*) 。
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                                                     '/home')
        fname = open(filename)
        # 读取选择的文件，并把文件内容放入文本编辑器。
        data = fname.read()
        self.textEdit.setText(data)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()