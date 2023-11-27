from PyQt5 import QtWidgets as QtW
from PyQt5.QtCore import QObject, pyqtSignal

from src.templates.footer.footer import Ui_footer

class Footer(QObject):
    def __init__(self):
        super().__init__()

        self.footer_widget = QtW.QWidget()
        self.footer_ui = Ui_footer()
        self.footer_ui.setupUi(self.footer_widget)

        self.footer_ui.btn_spending.setCheckable(True)

        self.footer_ui.btn_spending.clicked.connect(self.receber_sinal)

    def receber_sinal(self):
        print("Teste")
