from PyQt5 import QtWidgets as QtW

from src.templates.header.header import Ui_header

class Header:
    def __init__(self):
        self.header_widget = QtW.QWidget()
        self.header_ui = Ui_header()
        self.header_ui.setupUi(self.header_widget)
