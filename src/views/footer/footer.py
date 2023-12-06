from PyQt5 import QtWidgets as QtW
from PyQt5.QtCore import QObject, pyqtSignal

from src.templates.footer.footer import Ui_footer

class Footer(QObject):
    teste_sinal = pyqtSignal()

    def __init__(self):
        super(Footer, self).__init__()

        self.footer_widget = QtW.QWidget()
        self.footer_ui = Ui_footer()
        self.footer_ui.setupUi(self.footer_widget)

        #self.footer_ui.btn_spending.setCheckable(True)
