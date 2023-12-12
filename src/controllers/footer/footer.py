from PyQt5 import QtWidgets as QtW
from PyQt5.QtCore import QObject, pyqtSignal

from src.views.footer.footer import Footer
from src.views.main.view import MainView

from src.shared.definitions import DefinitionsFooter

class FooterController(QObject):
    def __init__(
        self,
        footer: Footer,
        main_view: MainView
    ):
        self.footer_ui = footer.footer_ui

        footer.button_clicked.connect(lambda button_id: self.handle_buttons(button_id))

    def handle_buttons(self, button_id: int):

        if(button_id == DefinitionsFooter.HOME.value):
            pass
            #self.footer.footer_ui.btn_spending.clicked.connect(lambda: self.handleContentCentral("SPENDING"))
            #self.footer.footer_ui.btn_home.clicked.connect(lambda: self.handleContentCentral("HOME"))

        # if(self.footer_ui.btn_home.isChecked()):
        #     print("já tá marcado")
        #     return
