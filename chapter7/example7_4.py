# -*- coding=UTF-8 -*-

# QComboBox 窗口组件允许用户从列表清单中选择。
# 这个例子中显示一个 QComboBox 和一个 QLabel 。组合框有5个选项的列表，他们是Linux发行版的名称。
# 标签显示从组合框选择的内容。
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 添加一个标签
        self.label = QtGui.QLabel("Ubuntu", self)

        # 添加一个下拉框并且添加若干选项
        combo = QtGui.QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Red Hat")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.label.move(50, 150)

        # 将下拉框的激活信号与自定义的函数槽连接
        self.connect(combo, QtCore.SIGNAL('activated(QString)'),
            self.onActivated)

        self.setGeometry(250, 200, 350, 250)
        self.setWindowTitle('QComboBox')

    def onActivated(self, text):
        self.label.setText(text)
        self.label.adjustSize()


def main():
    app = QtGui.QApplication([])
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
