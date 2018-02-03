# -*- coding=UTF-8 -*-

# 绘制点
# 点是可以绘制的最简单的图形对象，是窗口上的很小的一个区域。
# 在这个例子中，我们在客户区随机地绘制1000个红点。

import sys, random
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Points')

    # 重写窗口绘制事件
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    # 绘制函数
    def drawPoints(self, qp):
        # 使用红色初始化画笔
        qp.setPen(QtCore.Qt.red)
        size = self.size()

        # 在窗口内随机画1000个点
        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)


def main():
    app = QtGui.QApplication([])
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
