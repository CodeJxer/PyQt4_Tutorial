# -*- coding=UTF-8 -*-

# 在PyQt4教程的这部分中，我们讨论拖放操作。

# 拖放（Drag-and-drop）指的是图形用户界面（Graphical user interface）中，
# 在一个虚拟的对象上按着鼠标键将之拖曳到另一个地方或另一虚拟对象之上的动作
# （或是支持着这样的界面的技术）。一般而言，这可以用来产生很多动作，或是在
# 两个抽象对象当中产生各式各样的连接。

# 拖放操作功能是图形用户界面最明显的方面之一。拖放操作能使用户直观的做复杂的事情。

# 通常，我们可以拖放两类东西：数据或者一些图形对象。如果我们从一个程序拖动
# 图片到另一个，我们实际拖动了二进制数据。如果我们在Firefox中拖动标签页到另
# 一个地方，我们拖动了一个可视化组件。

import sys
from PyQt4 import QtGui


class Button(QtGui.QPushButton):
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)
        # 允许拖放数据
        self.setAcceptDrops(True)

    # 重写拖入事件
    def dragEnterEvent(self, e):
        # 接受文本数据， 否则忽略
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
    # 重写鼠标释放事件
    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 添加一个单行文本框， 并置为可接受拖拽的数据
        edit = QtGui.QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        # 添加一个按钮
        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple Drag & Drop')
        self.setGeometry(300, 300, 300, 150)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
