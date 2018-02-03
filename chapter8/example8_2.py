# -*- coding=UTF-8 -*-

# 在接下来的例子中，我们将演示如何使用鼠标右键拖放一个按钮窗口组件。

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Button(QtGui.QPushButton):
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

    # 重写鼠标移动事件
    def mouseMoveEvent(self, e):
        # 不是鼠标右键则忽略
        if e.buttons() != QtCore.Qt.RightButton:
            return

        mimeData = QtCore.QMimeData()

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.start(QtCore.Qt.MoveAction)

    # 重写鼠标点击事件
    def mousePressEvent(self, e):
        QtGui.QPushButton.mousePressEvent(self, e)
        if e.button() == QtCore.Qt.LeftButton:
            print 'press'


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 将窗口置为接受拖放数据
        self.setAcceptDrops(True)

        # 添加一个按钮
        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)

    # 重写拖入事件
    def dragEnterEvent(self, e):
        e.accept()

    # 重写鼠标释放事件
    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)

        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
