from PyQt5 import QtWidgets as QtW
from PyQt5.QtCore import QObject, pyqtSignal

from src.templates.footer.footer import Ui_footer

from src.shared.definitions import DefinitionsFooter

class FooterView(QObject):

    button_clicked = pyqtSignal(int)
    handle_content_central = pyqtSignal(int)

    def __init__(self):
        super(FooterView, self).__init__()

        self.footer_widget = QtW.QWidget()
        self.footer_ui = Ui_footer()
        self.footer_ui.setupUi(self.footer_widget)

        self.footer_widget.setMinimumHeight(60)
        self.footer_widget.setMaximumHeight(60)

        self.footer_ui.btn_home.clicked.connect(lambda: self.button_clicked.emit(DefinitionsFooter.HOME.value))
        self.footer_ui.btn_spending.clicked.connect(lambda: self.button_clicked.emit(DefinitionsFooter.EXPENSES.value))
