from PyQt5 import QtWidgets as QtW
from PyQt5.QtCore import QObject, pyqtSignal

from src.templates.footer.footer import Ui_footer

class Footer:
    def __init__(self):
        self.footer_widget = QtW.QWidget()
        self.footer_ui = Ui_footer()
        self.footer_ui.setupUi(self.footer_widget)
