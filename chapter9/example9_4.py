# -*- coding=UTF-8 -*-

# QPen
# QPen 是初级图形对象，用来绘制线条、曲线和矩形、椭圆、多边形或其他形状的轮廓。

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('penstyles')

    # 重写窗口绘制事件
    def paintEvent(self, e):
        qp = QtGui.QPainter()

        qp.begin(self)
        self.doDrawing(qp)
        qp.end()

    def doDrawing(self, qp):
        # 创建画笔
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)

        # 绘制不同的线性
        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(QtCore.Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(QtCore.Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(QtCore.Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(QtCore.Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        pen.setStyle(QtCore.Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()
