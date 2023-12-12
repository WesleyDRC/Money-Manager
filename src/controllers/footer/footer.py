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
        super(FooterController, self).__init__()

        self.footer = footer
        self.footer_ui = footer.footer_ui

        self.footer.button_clicked.connect(lambda button_id: self.handle_buttons(button_id))

    def handle_buttons(self, button_id: int):
        home_button_checked = self.footer_ui.btn_home.isChecked()
        expenses_button_checked = self.footer_ui.btn_spending.isChecked()

        print("home_button_checked " + str(home_button_checked))
        print("expenses_button_checked " + str(expenses_button_checked))

        if button_id == DefinitionsFooter.HOME.value:
            if not home_button_checked:
                self.footer_ui.btn_home.setChecked(True)
                self.footer_ui.btn_spending.setChecked(False)
            else:
                # Lógica a ser executada se o botão já estiver marcado
                self.footer_ui.btn_home.setChecked(True)
                self.footer_ui.btn_spending.setChecked(False)
                self.footer.handle_content_central.emit(DefinitionsFooter.HOME.value)

        elif button_id == DefinitionsFooter.EXPENSES.value:
            if not expenses_button_checked:
                print("EXPENSE")
                self.footer_ui.btn_home.setChecked(False)
                self.footer_ui.btn_spending.setChecked(True)
            else:
                # Lógica a ser executada se o botão já estiver marcado
                self.footer_ui.btn_home.setChecked(False)
                self.footer_ui.btn_spending.setChecked(True)
                self.footer.handle_content_central.emit(DefinitionsFooter.EXPENSES.value)
