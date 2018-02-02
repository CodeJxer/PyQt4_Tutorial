# -*- coding=UTF-8 -*-

# 窗口组件是应用程序的基本构建块。PyQt4编程工具包拥有范围广泛的各种窗口组件。
# 按钮、选择框、滑块、列表框等等，程序员工作所需要的一切。在教程的这部分中，
# 我们将介绍一些有用的窗口组件。

# QCheckBox （复选框） 是一个由两种状态的窗口组件。 On 和 Off 。他是一个带标签的框。
# 每当一个复选框被选中和或者清楚时，都将发射信号 stateChanged() 。

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('checkbox')

        # 构建 QCheckBox 。
        self.cb = QtGui.QCheckBox('show title', self)
        # 禁用 QCheckBox 的焦点。获有焦点的 QCheckBox 可以通过空格选择或者取消选择。
        self.cb.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb.move(10, 10)
        # 勾选复选框。设置窗口标题，必须选中复选框。默认情况下，不设置窗口标题，复选框设为未选择。
        self.cb.toggle()
        # 连接用户定义的changeTitle()到stateChanged()信号。changeTitle()方法将切换窗口标题。
        self.connect(self.cb, QtCore.SIGNAL('stateChanged(int)'),
                     self.changeTitle)

    def changeTitle(self, value):
        if self.cb.isChecked():
            self.setWindowTitle('checkbox')
        else:
            self.setWindowTitle('')

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()