# Model
from src.model.core.core import CoreModel

from src.views.footer.footer import FooterView
from src.views.core.core import Core
from src.views.limit_expense_graph.limit_expense_graph import LimitExpenseGraph
from src.views.limit_and_expense.limit_and_expense import LimitAndExpense

from src.shared.definitions import DefinitionsFooter
from src.shared.utils import Utils

from PyQt5 import QtWidgets as QtW
from PyQt5.QtCore import QObject, pyqtSignal

class CoreController(QObject):
    show_home = pyqtSignal()

    def __init__(
        self,
        core: Core,
        footer_view: FooterView,
        limit_expense_graph: LimitExpenseGraph,
        limit_and_expense: LimitAndExpense,
        core_lt
    ):
        super(CoreController, self).__init__()

        # Views
        self._footer_view = footer_view
        self._core_view = core
        self._limit_expense_graph_view = limit_expense_graph
        self._limit_and_expense_view = limit_and_expense

        # Model Core
        self._core_model = CoreModel()

        # Layout Objects
        self.widgets_limits_and_chart_layout = None
        self.core_layout = core_lt

        self.core_layouts()

    def core_layouts(self):
        self.widgets_limits_and_chart_layout = QtW.QVBoxLayout()
        self.widgets_limits_and_chart_layout.setSpacing(0)
        self.widgets_limits_and_chart_layout.setContentsMargins(0,0,0,0)

    def handle_content_central(self, screen):
        if(screen == DefinitionsFooter.HOME.value):
            self._footer_view.footer_ui.btn_home.setChecked(True)
            self._limit_expense_graph_view.draw_chart()
            self.position_elements("HOME")

        if(screen == DefinitionsFooter.EXPENSES.value):
            self.position_elements("SPENDING")

    def position_elements(self, screen):
        if(screen == "HOME"):
            self.widgets_limits_and_chart_layout.addStretch()
            self.widgets_limits_and_chart_layout.addWidget(self._limit_and_expense_view.limit_expense_widget)
            self.widgets_limits_and_chart_layout.addWidget(self._limit_expense_graph_view.view)
            self.widgets_limits_and_chart_layout.addStretch()

            self._limit_and_expense_view.limit_expense_widget.show()

            self.core_layout.addStretch()
            self.core_layout.addLayout(self.widgets_limits_and_chart_layout)
            self.core_layout.addStretch()

        if screen == "SPENDING":
            # Limpa o layout antes de adicionar novamente à self.core_layout, excluindo self.core.core_widget
            Utils.clear_layout(self.core_layout, self._core_view.core_widget)

            # Adiciona novamente à self.core_layout para atualizar a ordem de exibição
            self.core_layout.addWidget(self._core_view.core_widget)
