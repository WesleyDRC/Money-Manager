from PyQt5 import QtWidgets as QtW
from PyQt5.QtCore import QObject, pyqtSignal

from src.views.footer.footer import FooterView
from src.views.main.view import MainView

from src.shared.definitions import DefinitionsFooter

class FooterController(QObject):
    def __init__(
        self,
        footer_view: FooterView,
        main_view: MainView
    ):
        super(FooterController, self).__init__()

        self.footer = footer_view
        self.footer_ui = footer_view.footer_ui

        self.footer.button_clicked.connect(lambda button_id: self.handle_buttons(button_id))

    def handle_buttons(self, button_id: int):
        home_button_checked = self.footer_ui.btn_home.isChecked()
        expenses_button_checked = self.footer_ui.btn_spending.isChecked()

        if button_id == DefinitionsFooter.HOME.value:
            if not home_button_checked:
                self.footer_ui.btn_home.setChecked(True)
                self.footer_ui.btn_spending.setChecked(False)
            else:
                self.footer_ui.btn_home.setChecked(True)
                self.footer_ui.btn_spending.setChecked(False)
                self.footer.handle_content_central.emit(DefinitionsFooter.HOME.value)

        elif button_id == DefinitionsFooter.EXPENSES.value:
            if not expenses_button_checked:
                self.footer_ui.btn_home.setChecked(False)
                self.footer_ui.btn_spending.setChecked(True)
            else:
                self.footer_ui.btn_home.setChecked(False)
                self.footer_ui.btn_spending.setChecked(True)
                self.footer.handle_content_central.emit(DefinitionsFooter.EXPENSES.value)
