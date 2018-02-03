# -*- coding=UTF-8 -*-

# 当我们想要改变或者增强已存在的窗口组件时，或者准备从零开始创建自定义窗口组件时，
# 可以使用绘图。我们通过使用PyQt4工具包提供的绘图API来绘图。
# 绘图在 paintEvent() 方法中进行。绘制代码在 QPainter 对象的 begin() 和 end() 之间。

# 绘制文本
# 我们从在窗口客户区绘制一些Unicode文本开始。

from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Draw Text')

        # 预设文本
        self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
  \u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
  \u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'

    # 重写绘画事件
    def paintEvent(self, event):
        # 在绘画事件中绘画
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    # 绘制文本
    def drawText(self, event, qp):
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)


def main():
    app = QtGui.QApplication([])
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
