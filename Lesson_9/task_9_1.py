import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class TrafficLight(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TrafficLight')
        self.setGeometry(650, 300, 400, 300)
        self.but = QtWidgets.QPushButton(self)
        self.but.move(150, 120)
        self._color = 'grey'
        self.but.setStyleSheet(f'background-color: {self._color};')
        self.but.clicked.connect(self.running)

    def running(self):
        # while True:
        self._color = 'red'
        self.but.setStyleSheet(f'background-color: {self._color};')
        print('red')
        time.sleep(7)
        self._color = 'yellow'
        self.but.setStyleSheet(f'background-color: {self._color};')
        print('yellow')
        time.sleep(2)
        self._color = 'green'
        self.but.setStyleSheet(f'background-color: {self._color};')
        print('green')
        time.sleep(10)
        self._color = 'yellow'
        self.but.setStyleSheet(f'background-color: {self._color};')
        print('yellow')
        time.sleep(2)


app = QApplication([])
window = TrafficLight()
# window.running()
window.show()
app.exec_()
# window.running()



# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
# from PyQt5.QtGui import QPalette
# from PyQt5.QtCore import Qt
# import time
# import PyQt5
#
#
# class TrafficLight(PyQt5):
#     def __init__(self):
#         super().__init__(self)
#         # self.__color = None
#
#         self.__color = None
#
#     def rotation(self):
#         app = QApplication([])
#         app.setStyle('Fusion')
#         window = QWidget()
#         layout = QVBoxLayout()
#         layout.addWidget(QPushButton())
#         pallet = QPalette()
#         # while True:
#         pallet.setColor(QPalette.Button, Qt.red)
#         app.setPalette(pallet)
#         # time.sleep()
#         window.setLayout(layout)
#         window.show()
#         app.exec_()
#         # while True:
#         # if self.__color is None:
#         #     self.__color = Qt.red
#         #     return self.__color, 7
#         # elif self.__color == Qt.red:
#         #     self.__color = Qt.yellow
#         #     return self.__color, 2
#         # # elif self.__color == Qt.yellow
#
#         # self.__color = Qt.red
#             # print('красный')
#             # pallet.setColor(QPalette.Button, self.__color)
#         # return self.__color
#             # time.sleep(7)
#             # self.__color = Qt.yellow
#             # print('жёлтый')
#             # return self.__color
#             # time.sleep(2)
#             # self.__color = Qt.green
#             # print('зелёный')
#             # return self.__color
#             # time.sleep(5)
#             # self.__color = Qt.yellow
#             # print('жёлтый')
#             # return self.__color
#             # time.sleep(2)
#
#
# traffic_light = TrafficLight()
# print(traffic_light.rotation())
#
# # app = QApplication([])
# # app.setStyle('Fusion')
# # window = QWidget()
# # layout = QVBoxLayout()
# # layout.addWidget(QPushButton())
# # pallet = QPalette()
# # pallet.setColor(QPalette.Button, Qt.red)
# # app.setPalette(pallet)
# # window.setLayout(layout)
# # window.show()
# # app.exec_()
#
#
