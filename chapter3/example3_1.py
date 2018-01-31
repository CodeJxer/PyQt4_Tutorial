# -*- coding=UTF-8 -*-

# 编程中的一个重要事情是布局管理，布局管理是如何在窗体上摆放窗口组件。可以有两种方式进行管理：绝对定位或使用布局类。

# 在绝对定位下程序员用像素指定每个控件的位置和尺寸。使用绝对定位时，你必须理解几件事情。
#    - 如果你调整窗体的大小，组件的尺寸和位置并不会改变
#    - 在不同的平台上，程序可能看起来不一样
#    - 改变程序的字体可能破坏布局
#    - 如果你决定改变你的布局，你必须完全重做你的布局，这将是乏味并且浪费时间的

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.initUI()

    def initUI(self):
        # 我们简单的调用 move() 方法来定位组件。在我们的 QLabel 例子中，我们用x和y坐标来定位。
        # 坐标系统从左上角开始，x值从左到右增长，y值从上到下增长。
        label1 = QtGui.QLabel('Zetcode', self)
        label1.move(15, 10)

        label2 = QtGui.QLabel('tutorials for programmers', self)
        label2.move(35, 40)

        self.setWindowTitle('Absolute')
        self.resize(250, 150)


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())