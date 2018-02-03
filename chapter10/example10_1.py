# -*- coding=UTF-8 -*-

# 自定义窗口组件
# 你是否曾经看着应用程序并思考特定的GUI项是如何产生的？大概每位程序员都这样过。然后你能看到你喜欢的GUI
# 库提供的一系列窗口组件，但是你无法找到它。工具包通常仅仅提供最常用的窗口组件，比如按钮、文本组件、滑
# 块等等。没有工具包能够提供一切可能的组件。

# 实际上有两种工具包，轻量级和重量级。FLTK工具包是一种轻量级的工具包，它仅仅提供非常基本的组件并假设程
# 序员能够自己创建更复杂的组件。PyQt4属于重量级，它有很多窗口组件，但是并不提供非常专业化的窗口组件。
# 比如速度计窗口组件，用来度量烧录的CD的容量（可在Nero中找到）。也没有包含常用的图表。

# 程序员必须自己创建这些窗口组件，通过工具包提供的绘画工具来创建。有两种方法，修改或增强已有的组件，或
# 者从零开始创建。

# 烧录窗口组件

import sys
from PyQt4 import QtGui, QtCore


# 自定义组件
class BurningWidget(QtGui.QWidget):
    def __init__(self):
        super(BurningWidget, self).__init__()

        self.initUI()

    def initUI(self):
        self.setMinimumSize(1, 30)              # 设置宽度
        self.value = 75                         # 设置初始值
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]     # 设置刻度列表

        # 将updateBurningWidget信号和setValue函数槽连接
        self.connect(self, QtCore.SIGNAL("updateBurningWidget(int)"),
            self.setValue)

    def setValue(self, value):
        self.value = value                      # 更改数值

    # 重写窗口的绘画事件
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self, qp):
        font = QtGui.QFont('Serif', 7, QtGui.QFont.Light)
        qp.setFont(font)

        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w / 10.0))

        till = int(((w / 750.0) * self.value))
        full = int(((w / 750.0) * 700))

        if self.value >= 700:
            qp.setPen(QtGui.QColor(255, 255, 255))
            qp.setBrush(QtGui.QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QtGui.QColor(255, 175, 175))
            qp.setBrush(QtGui.QColor(255, 175, 175))
            qp.drawRect(full, 0, till-full, h)
        else:
            qp.setPen(QtGui.QColor(255, 255, 255))
            qp.setBrush(QtGui.QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)

        pen = QtGui.QPen(QtGui.QColor(20, 20, 20), 1,
            QtCore.Qt.SolidLine)

        qp.setPen(pen)
        qp.setBrush(QtCore.Qt.NoBrush)
        qp.drawRect(0, 0, w-1, h-1)

        j = 0
        for i in range(step, 10*step, step):
            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            qp.drawText(i-fw/2, h/2, str(self.num[j]))
            j = j + 1


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 添加滑块
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slider.setFocusPolicy(QtCore.Qt.NoFocus)
        slider.setRange(1, 750)
        slider.setValue(75)
        slider.setGeometry(30, 40, 150, 30)

        self.wid = BurningWidget()

        # 将滑块的valueChanged信号和changeValue函数槽连接
        self.connect(slider, QtCore.SIGNAL('valueChanged(int)'),
            self.changeValue)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Burning')

    def changeValue(self, value):
        # 发射updateBurningWidget信号
        self.wid.emit(QtCore.SIGNAL("updateBurningWidget(int)"), value)
        self.wid.repaint()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
