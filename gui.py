from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setGeometry(500, 500, 500, 300)

        start_button = QPushButton("Start recording", self)
        start_button.setGeometry(200,0,100,50)
        stop_button = QPushButton("Stop recording", self)
        stop_button.setGeometry(200,150,100,50)

        start_button.clicked.connect(self.start_func)
        stop_button.clicked.connect(self.end_func)



    def start_func(self):
        print("hello world :)")

    def end_func(self):
        print("goodbye world :(")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show() 

    app.exec()
