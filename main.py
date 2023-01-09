# 这里绘制的是UI的主界面
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QDesktopWidget,
                             QMessageBox, QMainWindow, QGridLayout, QLabel)
from PyQt5.QtGui import QIcon, QPixmap
import Frontend.Page as Page
import Frontend.UI as UI
import qtawesome


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.Init()

    def Init(self):
        grid = QGridLayout()
        # 这个叫widget的是主widget。左侧为一列功能键，右侧为页面
        self.widget = QWidget()
        self.widget.setObjectName("main")
        self.widget.setLayout(grid)
        self.setCentralWidget(self.widget)
        grid.setSpacing(15)

        self.page_input = Page.page(grid, self)
        UI.InitUI(self.page_input)

        # # 给布局添加上左侧功能键和LOGO
        # logo = QLabel(self)
        # directory = "img/logo2.png"
        # pix = QPixmap(directory)
        # logo.setPixmap(pix)
        # grid.addWidget(logo, 1, 0, 3, 1)

        # # 设置标题logo
        # self.setWindowIcon(QIcon(directory))
        # 居中并绘制
        self.resize(1440, 820)
        self.center()
        self.setWindowTitle("期权计算器")
        self.show()

    # 启动时居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
