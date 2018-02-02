# -*- coding=UTF-8 -*-

# 滑块是由一个简单的滑柄的窗口组件。该滑柄可以前后拖动，通过这种方式我们可以为特定任务选择值。
# 有时候使用滑块比简单提供数值或使用微调框(spin box)更自然。 QLabel 显示文字或图像。

# 该例子中我们将显示一个滑块和一个标签。这次，标签将显示滑块对应数值，滑块用来控制标签。

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 创建一个水平 QSlider 。
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slider.setFocusPolicy(QtCore.Qt.NoFocus)
        slider.setGeometry(30, 40, 100, 30)
        # 连接valueChanged信号到自定义的changeValue()方法。
        self.connect(slider, QtCore.SIGNAL('valueChanged(int)'),
                     self.changeValue)

        self.label = QtGui.QLabel(self)
        self.label.setText('0')
        self.label.setGeometry(135, 45, 30, 20)
        self.setGeometry(300, 300, 250, 150)

    def changeValue(self, value):
        # 基于滑块的值，我们设置数值到标签上。
        self.label.setText(str(value))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
