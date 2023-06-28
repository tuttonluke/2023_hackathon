from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setGeometry(500, 500, 300, 200)
        self.setStyleSheet('background-color: black;')

        start_button = QPushButton("start recording", self)
        start_button.setGeometry(100,25,100,50)
        start_button.setStyleSheet('background-color: white;')
        start_button.setFont(QFont('Arial', 10))
        stop_button = QPushButton("stop recording", self)
        stop_button.setGeometry(100,125,100,50)
        stop_button.setStyleSheet('background-color: white;')
        stop_button.setFont(QFont('Arial', 10))

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
