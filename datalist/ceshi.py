import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal
from common import base_path


class TestRunner(QThread):
    new_output = pyqtSignal(str)  # 定义信号

    def run(self):
        # 使用 subprocess 运行 pytest
        process = subprocess.Popen(
            ['pytest', base_path("testcase"), '-v', '-s', '--tb=short'],  # 这里可以添加其他 pytest 参数
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            encoding='utf-8'
        )

        # 实时读取输出
        for line in process.stdout:
            self.new_output.emit(line)  # 发射信号，将输出发送到界面

        process.stdout.close()
        process.wait()  # 等待进程结束


class TestRunerWindow(QMainWindow):
    def __init__(self, host_value, token_value):
        super().__init__()
        self.setWindowTitle("pytest 实时输出示例")
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)  # 设置为只读
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        button = QPushButton("开始测试", self)
        button.clicked.connect(self.start_testing)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_testing(self):
        self.test_runner = TestRunner()  # 创建 TestRunner 线程
        self.test_runner.new_output.connect(self.update_text)  # 连接信号到槽
        self.test_runner.start()  # 启动线程

    def update_text(self, text):
        self.text_edit.append(text)  # 更新 QTextEdit


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestRunerWindow()
    window.show()
    sys.exit(app.exec_())
