from PyQt5 import QtWidgets as QtW
from PyQt5.QtCore import QObject

class Core(QObject):
    def __init__(self):
        self.core_widget = QtW.QWidget()

        self.core_widget.setObjectName("content")
        self.core_widget.setStyleSheet("#content { background-color: #232327}")
