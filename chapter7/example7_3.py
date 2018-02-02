# -*- coding=UTF-8 -*-

# QSplitter 使得用户可以通过拖动子窗口组件的边界来控制子窗口组件的尺寸。
# 在我们的例子中，我们显示由两个分离器组织的三个 QFrame 窗口组件。
# 例子中有三个框架窗口组件和两个分离器。
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 创建一个盒布局
        hbox = QtGui.QHBoxLayout(self)

        # 在左上方创建一个面板
        topleft = QtGui.QFrame(self)
        topleft.setFrameShape(QtGui.QFrame.StyledPanel)

        # 在右上方创建一个面板
        topright = QtGui.QFrame(self)
        topright.setFrameShape(QtGui.QFrame.StyledPanel)

        # 在底部创建一个面板
        bottom = QtGui.QFrame(self)
        bottom.setFrameShape(QtGui.QFrame.StyledPanel)

        # 创建一个左右的分隔栏
        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        # 创建一个上下的分隔栏
        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        # 将上下的分隔栏以及被分隔的面板放到盒布局中
        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setWindowTitle('QSplitter')
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        self.setGeometry(250, 200, 350, 250)


def main():
    app = QtGui.QApplication([])
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
