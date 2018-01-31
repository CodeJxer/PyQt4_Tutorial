# -*- coding=UTF-8 -*-

# 这是一个演示PyQt4信号和槽的简单例子。
# connec方法有4个参数，
#   sender 是发送信号的对象，
#   signal 是发射的信号，
#   receiver 是接收信号的对象，
#   slog 是对信号反应的方法。
import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        lcd = QtGui.QLCDNumber(self)
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        # 这里我们连接滑块slider的valueChanged()信号到LCD数字的display()槽。
        self.connect(slider,    QtCore.SIGNAL('valueChanged(int)'),
                     lcd,       QtCore.SLOT('display(int)'))

        self.setWindowTitle('signal && slot')
        self.resize(550, 450)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())