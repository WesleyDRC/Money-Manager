from PyQt5 import QtWidgets as QtW
from PyQt5.QtGui import QBrush, QColor, QPen

from src.views.main.view import MainView

# Templates
from src.templates.header.header import Ui_header
from src.templates.footer.footer import Ui_footer
from src.templates.core.components.limitAndExpense.limit_and_expense import Ui_limitAndExpense

from src.shared.parameters import Parameters

from src.templates.core.components.limitExpenseGraph.limit_expense_graph import LimitExpenseGraph

class MainController:
  def __init__(
    self,
    app: QtW.QApplication,
    view: MainView
  ):
    # Controller Objects
    self.header_controller = None
    self.footer_controller = None

    # UI Objects
    self.header_ui = None
    self.footer_ui = None
    self.limit_expense_ui = None

    # Widgets Objects
    self.header_widget = None
    self.footer_widget = None
    self.limit_expense_widget = None

    # Layout Objects
    self.widgets_limits_and_chart_layout = None
    self.header_layout = None
    self.content_layout = None
    self.footer_layout = None

    self.limit_expense_graph = None

    self.main_view = view

    self.setup_ui_objects()

  def setup_ui_objects(self):
    self.header_widget = QtW.QWidget(self.main_view)
    self.header_ui = Ui_header()
    self.header_ui.setupUi(self.header_widget)

    self.content_widget = QtW.QWidget(self.main_view)

    self.footer_widget = QtW.QWidget(self.main_view)
    self.footer_ui = Ui_footer()
    self.footer_ui.setupUi(self.footer_widget)

    self.limit_expense_widget = QtW.QWidget(self.main_view)
    self.limit_expense_ui = Ui_limitAndExpense()
    self.limit_expense_ui.setupUi(self.limit_expense_widget)

    self.configure_interface()

  def configure_interface(self):
    self.hide_elements()
    self.layout_all_ui()
    self.configure_layout()

  def layout_all_ui(self):
    self.header_layout = QtW.QVBoxLayout()
    self.header_layout.addWidget(self.header_widget)

    self.content_layout = QtW.QVBoxLayout()
    self.content_layout.addWidget(self.content_widget)

    self.footer_layout = QtW.QVBoxLayout()
    self.footer_layout.addWidget(self.footer_widget)

    self.main_view.main_layout.addLayout(self.header_layout)
    self.main_view.main_layout.addLayout(self.content_layout)
    self.main_view.main_layout.addLayout(self.footer_layout)

  def configure_layout(self):
    self.main_view.showMaximized()
    self.handleContentCentral("HOME")


  def handleContentCentral(self, screen):
    self.content_widget.setObjectName("content")
    self.content_widget.setStyleSheet("#content { background-color: #FF0000}")

    if(screen == "HOME"):
      # CHART
      # Essa eh a cena onde inserimos os componentes/itens
      self.scene = QtW.QGraphicsScene()

      # Widget que exibe a cena
      self.view = QtW.QGraphicsView(self.scene)

      self.view.setObjectName("circle")
      self.view.setStyleSheet("#circle {background-color: #232327; border: none}")

      self.widgets_limits_and_chart_layout = QtW.QVBoxLayout()
      self.widgets_limits_and_chart_layout.setSpacing(0)
      self.widgets_limits_and_chart_layout.setContentsMargins(0,0,0,0)

      self.limit_expense_graph = LimitExpenseGraph()

      value1 = 0.9
      value2 = 0.1

      # Angulo inicial e final dos setores
      start_angle = 0
      end_angle1 = 360 * value1
      end_angle2 = 360 * (value1 + value2)

      # Desenha o primeiro setor
      self.limit_expense_graph.draw_sector(self.scene, start_angle, end_angle1, QColor("#77AE7D"))

      # Desenha o segundo setor
      self.limit_expense_graph.draw_sector(self.scene, end_angle1, end_angle2, QColor("#e74c3c"))

      # Desenha um círculo no meio
      self.limit_expense_graph.draw_circle_in_middle(self.scene, QColor("#232327"))

      self.widgets_limits_and_chart_layout.addWidget(self.limit_expense_widget)
      self.widgets_limits_and_chart_layout.addWidget(self.view)

      self.limit_expense_widget.show()

      self.content_layout.addStretch()
      self.content_layout.addLayout(self.widgets_limits_and_chart_layout)
      self.content_layout.addStretch()

  def hide_elements(self):
    self.limit_expense_widget.hide()
