# -*- coding=UTF-8 -*-

# QPixmap 是处理图像的窗口组件之一，非常适合在屏幕上显示图像。
# 在我们的代码示例里，我们使用 QPixmap 在窗口中显示图像。

from PyQt4 import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 创建一个盒布局
        hbox = QtGui.QHBoxLayout(self)
        # 创建一个QPixmap对象
        pixmap = QtGui.QPixmap('guitar.jpg')

        # 添加一个标签
        label = QtGui.QLabel(self)
        label.setPixmap(pixmap)

        # 将标签添加到盒布局中
        hbox.addWidget(label)
        self.setLayout(hbox)

        self.setWindowTitle('show guitar')
        self.move(250, 200)

def main():
    app = QtGui.QApplication([])
    ex = Example()
    ex.show()
    app.exec_()

if __name__ == '__main__':
    main()
