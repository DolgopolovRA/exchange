from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt
import time


class TrafficLight:
    def __init__(self):
        # self.__color = None

        self.__color = None

    def rotation(self):
        # while True:
        if self.__color is None:
            self.__color = Qt.red
            return self.__color, 7
        elif self.__color == Qt.red:
            self.__color = Qt.yellow
            return self.__color, 2
        # elif self.__color == Qt.yellow

        # self.__color = Qt.red
            # print('красный')
            # pallet.setColor(QPalette.Button, self.__color)
        # return self.__color
            # time.sleep(7)
            # self.__color = Qt.yellow
            # print('жёлтый')
            # return self.__color
            # time.sleep(2)
            # self.__color = Qt.green
            # print('зелёный')
            # return self.__color
            # time.sleep(5)
            # self.__color = Qt.yellow
            # print('жёлтый')
            # return self.__color
            # time.sleep(2)


traffic_light = TrafficLight()
# print(traffic_light.rotation())
app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton())
pallet = QPalette()
while True:
    # res = traffic_light.rotation()
    # print(res)
    color, time_z = traffic_light.rotation()
    pallet.setColor(QPalette.Button, color)
    app.setPalette(pallet)
    time.sleep(time_z)
    window.setLayout(layout)
    window.show()
app.exec_()
# app = QApplication([])
# app.setStyle('Fusion')
# window = QWidget()
# layout = QVBoxLayout()
# layout.addWidget(QPushButton())
# pallet = QPalette()
# pallet.setColor(QPalette.Button, Qt.red)
# app.setPalette(pallet)
# window.setLayout(layout)
# window.show()
# app.exec_()


