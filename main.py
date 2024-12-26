import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# from pyqt5.window import Ui_MainWindow      # example这里是你的命名文件
from datalist.ceshi2 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())



