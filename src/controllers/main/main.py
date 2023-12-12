from PyQt5 import QtWidgets as QtW
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QObject, pyqtSignal

from src.views.main.view import MainView

# Interfaces
from src.views.header.header import Header
from src.views.core.core import Core
from src.views.footer.footer import Footer
from src.views.limit_and_expense.limit_and_expense import LimitAndExpense
from src.views.limit_expense_graph.limit_expense_graph import LimitExpenseGraph

from src.shared.parameters import Parameters

from src.shared.definitions import DefinitionsFooter

from src.shared.utils import Utils
from typing import Union

# Controllers
from src.controllers.core.core import CoreController
from src.controllers.footer.footer import FooterController


class MainController(QObject):

  show_home = pyqtSignal()

  def __init__(
    self,
    app: QtW.QApplication,
    view: MainView
  ):

    super(MainController, self).__init__()
    # Controller Objects
    self.header_controller = None
    self.footer_controller = None
    self.core_controller = None

    # Interface Objects
    self.header = None
    self.core = None
    self.limit_and_expense = None
    self.limit_expense_graph = None
    self.footer = None

    # Layout Objects
    self.header_layout = None
    self.core_layout = None
    self.footer_layout = None

    # Interface principal onde os Widgets são inseridos
    self.main_view = view

    # Call methods to show interface
    self.configure_interface()

    # Instantiate controllers
    self.init_controllers()

    self.show_home.emit()

  def configure_interface(self):
    self.init_views()
    self.hide_elements()
    self.layout_all_ui()
    self.configure_layout()

  def init_views(self):
    self.header = Header()

    self.footer = Footer()

    self.core = Core()

    self.limit_and_expense = LimitAndExpense()

    self.limit_expense_graph = LimitExpenseGraph()

  def layout_all_ui(self):
    self.header_layout = QtW.QVBoxLayout()
    self.header_layout.addWidget(self.header.header_widget)

    self.core_layout = QtW.QHBoxLayout()
    self.core_layout.addWidget(self.core.core_widget)

    self.footer_layout = QtW.QVBoxLayout()
    self.footer_layout.addWidget(self.footer.footer_widget)

    self.main_view.main_layout.addLayout(self.header_layout)
    self.main_view.main_layout.addLayout(self.core_layout)
    self.main_view.main_layout.addLayout(self.footer_layout)

  def configure_layout(self):
    self.main_view.showMaximized()

  def hide_elements(self):
    self.limit_and_expense.limit_expense_widget.hide()

  def init_controllers(self):
    self.core_controller = CoreController(self.core, self.footer, self.limit_expense_graph, self.limit_and_expense, self.core_layout)
    self.footer_controller = FooterController(self.footer, self.main_view)

    self.show_home.connect(lambda: self.core_controller.handle_content_central(DefinitionsFooter.HOME.value))
