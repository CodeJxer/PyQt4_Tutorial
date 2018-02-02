# -*- coding=UTF-8 -*-

# 从 QtCore.QObject继承的对象可以发射信号。如果点击按钮，将产生一个clicked()信号。
# 在接下来的例子中可以看到如何发射信号。

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 这里我们把手工创建的closeEmitApp()信号和close()槽连接。
        self.connect(self, QtCore.SIGNAL('closeEmitApp()'),
                     QtCore.SLOT('close()'))

        self.setWindowTitle('emit')
        self.resize(250, 150)

    def mousePressEvent(self, event):
        # 通过emit()方法发射自定义信号。
        self.emit(QtCore.SIGNAL('closeEmitApp()'))

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())