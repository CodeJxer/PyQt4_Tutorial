# -*- coding=UTF-8 -*-

# QLineEdit 窗口组件用来输入或者编辑单行纯文本，有撤销/重做，剪切/粘贴和拖放功能。
# 该例子现在一个单行编辑器和一个标签。在单行编辑器中键入的文字会立即显示在标签中。

from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 添加标签
        self.label = QtGui.QLabel(self)
        # 添加文本框
        edit = QtGui.QLineEdit(self)

        # 放置文本框和标签
        edit.move(60, 100)
        self.label.move(60, 40)

        # 将文本框的文本改动信号和自定义的onChanged函数槽连接
        self.connect(edit, QtCore.SIGNAL('textChanged(QString)'),
                     self.onChanged)

        self.setWindowTitle('QLineEdit')
        self.setGeometry(250, 200, 350, 250)

    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()


def main():
    app = QtGui.QApplication([])
    exm = Example()
    exm.show()
    app.exec_()


if __name__ == '__main__':
    main()
