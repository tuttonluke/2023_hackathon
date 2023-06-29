from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import speech_to_text

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        window_x = 500
        window_y = 500
        window_width = 1000
        window_height = 1000

        button_x = 250
        button_width = 500
        button_height = 200

        text_font_size = 15
        
        self.setWindowTitle("My App")
        self.setGeometry(window_x, window_y, window_width, window_height)
        self.setStyleSheet('background-color: black;')

        start_button = QPushButton("Start Recording", self)
        start_button.setGeometry(button_x, 125, button_width, button_height)
        start_button.setStyleSheet('background-color: white;')
        start_button.setFont(QFont('Arial', text_font_size))
        stop_button = QPushButton("Stop Recording", self)
        stop_button.setGeometry(button_x, 425, button_width, button_height)
        stop_button.setStyleSheet('background-color: white;')
        stop_button.setFont(QFont('Arial', text_font_size))

        self.streamer = speech_to_text.Streamer()

        start_button.clicked.connect(self.start_func)
        stop_button.clicked.connect(self.end_func)



    def start_func(self):
        self.streamer.start_recording()
        
    def end_func(self):
        self.streamer.stop_recording()
        self.streamer.play_audio()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show() 

    app.exec()
