# -*- coding=UTF-8 -*-

# 进度条使用来处理长时间任务的窗口组件，当看到它的动画时，用户就知道我们的任务正在进行中。
# 在PyQt4工具包中， QProgressBar 窗口组件提供水平或者垂直的进度条。任务被分成一些阶段。
# 程序员可以为进度条设置最小值和最大值。默认是0，99.

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 添加一个QProgressBar 。
        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        # 添加一个按钮
        self.button = QtGui.QPushButton('Start', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(40, 80)

        # 将按钮的点击信号和自定义的doAction函数连接
        self.connect(self.button, QtCore.SIGNAL('clicked()'),
                     self.doAction)

        # 添加定时器对象
        self.timer = QtCore.QBasicTimer()
        self.step = 0

        self.setWindowTitle('ProgressBar')
        self.setGeometry(300, 300, 250, 150)

    # 重写定时器事件
    def timerEvent(self, event):
        if self.step >= 100:        # 超过100
            self.timer.stop()       # 停止定时器
            return

        self.step = self.step + 1   # 定时器增加1
        self.pbar.setValue(self.step)   # 将进度条的数值置为定时器的step数

    def doAction(self):             # 切换开关
        if self.timer.isActive():    # 激活状态
            self.timer.stop()         # 转换定时器为stop
            self.button.setText('Start')    # 更换按钮文字
        else:
            # 通过调用 start() 方法加载定时器事件，该方法有两个参数，
            # 超时时间（ timeout ）和
            # 接受事件的对象（ object ）。
            self.timer.start(100, self)
            self.button.setText('Stop')

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()