import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import threading


class TrafficLight(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TrafficLight')
        self.setGeometry(650, 300, 400, 300)
        self.but = QtWidgets.QPushButton(self)
        self.but.move(150, 120)
        self._color = 'grey'
        self.stop = 1
        self.but.setStyleSheet(f'background-color: {self._color};')
        self.but.clicked.connect(self.stop_circle)

    def stop_circle(self):
        self.stop = 0

    def running(self):
        while self.stop:
            self._color = 'red'
            self.but.setStyleSheet(f'background-color: {self._color};')
            time.sleep(7)
            self._color = 'yellow'
            self.but.setStyleSheet(f'background-color: {self._color};')
            time.sleep(2)
            self._color = 'green'
            self.but.setStyleSheet(f'background-color: {self._color};')
            time.sleep(5)
            self._color = 'yellow'
            self.but.setStyleSheet(f'background-color: {self._color};')
            time.sleep(2)


app = QApplication([])
window = TrafficLight()
t = threading.Thread(target=window.running, args=())
t.start()
window.show()
app.exec_()
window.stop_circle()
t.join()
