from PyQt5 import QtWidgets as QtW

from src.templates.core.components.limit_and_expense.limit_and_expense import Ui_limitAndExpense

class LimitAndExpense:
    def __init__(self):
        self.limit_expense_widget = QtW.QWidget()
        self.limit_expense_ui = Ui_limitAndExpense()
        self.limit_expense_ui.setupUi(self.limit_expense_widget)
