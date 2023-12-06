from PyQt5 import QtWidgets as QtW
from PyQt5.QtGui import QColor

from src.views.main.view import MainView

# Interfaces
from src.views.header.header import Header
from src.views.footer.footer import Footer
from src.views.limit_and_expense.limit_and_expense import LimitAndExpense
from src.views.limit_expense_graph.limit_expense_graph import LimitExpenseGraph

from src.shared.parameters import Parameters

from src.shared.utils import Utils
from typing import Union

class MainController:
  def __init__(
    self,
    app: QtW.QApplication,
    view: MainView
  ):
    # Controller Objects
    self.header_controller = None
    self.footer_controller = None

    # Interface Objects
    self.header = None
    self.limit_and_expense = None
    self.limit_expense_graph = None
    self.footer = None

    # Layout Objects
    self.widgets_limits_and_chart_layout = None
    self.header_layout = None
    self.content_layout = None
    self.footer_layout = None

    self.main_view = view

    self.setup_ui_objects()

  def init_footer(self):
    self.footer = Footer()

    self.footer.footer_ui.btn_spending.clicked.connect(lambda: self.handleContentCentral("SPENDING"))
    self.footer.footer_ui.btn_home.clicked.connect(lambda: self.handleContentCentral("HOME"))
    print("chegou")

  def setup_ui_objects(self):
    self.header = Header()

    self.content_widget = QtW.QWidget(self.main_view)

    self.limit_and_expense = LimitAndExpense()

    self.init_footer()

    self.configure_interface()

  def configure_interface(self):
    self.hide_elements()
    self.layout_all_ui()
    self.configure_layout()

  def layout_all_ui(self):
    self.header_layout = QtW.QVBoxLayout()
    self.header_layout.addWidget(self.header.header_widget)

    self.content_layout = QtW.QHBoxLayout()
    self.content_layout.addWidget(self.content_widget)

    self.footer_layout = QtW.QVBoxLayout()
    self.footer_layout.addWidget(self.footer.footer_widget)

    self.main_view.main_layout.addLayout(self.header_layout)
    self.main_view.main_layout.addLayout(self.content_layout)
    self.main_view.main_layout.addLayout(self.footer_layout)

  def configure_layout(self):
    self.main_view.showMaximized()
    self.handleContentCentral("HOME")

  def handleContentCentral(self, screen):
    self.content_widget.setObjectName("content")
    self.content_widget.setStyleSheet("#content { background-color: #232327}")

    if(screen == "HOME"):
      self.limit_expense_graph = LimitExpenseGraph()
      self.draw_chart()
      self.position_elements("HOME")

    if(screen == "SPENDING"):
      self.position_elements("SPENDING")

  def hide_elements(self):
    self.limit_and_expense.limit_expense_widget.hide()

  def draw_chart(self):
      # This is the scene where insert the components/items
      self.scene = QtW.QGraphicsScene()

      # Widget that shows the scene
      self.view = QtW.QGraphicsView(self.scene)

      # Style chart
      self.view.setObjectName("chart")
      self.view.setStyleSheet("#chart {background-color: #232327; border: none}")
      self.widgets_limits_and_chart_layout = QtW.QVBoxLayout()
      self.widgets_limits_and_chart_layout.setSpacing(0)
      self.widgets_limits_and_chart_layout.setContentsMargins(0,0,0,0)

      expense = 0.9
      limit = 0.1

      # Angulo inicial e final dos setores
      start_angle = 0
      end_angle1 = 360 * expense
      end_angle2 = 360 * (expense + limit)

      # Desenha o primeiro setor
      self.limit_expense_graph.draw_sector(self.scene, start_angle, end_angle1, QColor("#77AE7D"))

      # Desenha o segundo setor
      self.limit_expense_graph.draw_sector(self.scene, end_angle1, end_angle2, QColor("#e74c3c"))

      # Desenha um circulo no meio
      self.limit_expense_graph.draw_circle_in_middle(self.scene, QColor("#232327"))

  def position_elements(self, screen):
    if(screen == "HOME"):
      self.widgets_limits_and_chart_layout.addStretch()
      self.widgets_limits_and_chart_layout.addWidget(self.limit_and_expense.limit_expense_widget)
      self.widgets_limits_and_chart_layout.addWidget(self.view)
      self.widgets_limits_and_chart_layout.addStretch()

      self.limit_and_expense.limit_expense_widget.show()

      self.content_layout.addStretch()
      self.content_layout.addLayout(self.widgets_limits_and_chart_layout)
      self.content_layout.addStretch()

    if screen == "SPENDING":
        # Move self.content_widget para a frente
        self.content_widget.raise_()

        # Limpa o layout antes de adicionar novamente à self.content_layout, excluindo self.content_widget
        self.clear_layout(self.content_layout, self.content_widget)

        # Adiciona novamente à self.content_layout para atualizar a ordem de exibição
        self.content_layout.addWidget(self.content_widget)

  def clear_layout(self, layout: Union[QtW.QVBoxLayout, QtW.QHBoxLayout], exclude_object=None):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        layout_next = item.layout()

        if(widget and widget != exclude_object):
          widget.hide()
        elif(layout_next):
          self.clear_layout(layout_next, exclude_object)
