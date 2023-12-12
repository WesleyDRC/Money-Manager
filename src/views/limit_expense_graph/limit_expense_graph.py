from PyQt5 import QtWidgets as QtW
from PyQt5.QtGui import QBrush, QColor, QPen

class LimitExpenseGraph:
    def __init__(self):
        self.view = None
        self.scene = None

    def draw_sector(self, widget: QtW.QGraphicsScene, start_angle, end_angle, color):
        sector = widget.addEllipse(50, 50, 300, 300, QPen(QColor("#FFFFFF"), 5), QBrush(color))
        sector.setStartAngle(int(start_angle * 16))
        sector.setSpanAngle(int((end_angle - start_angle) * 16))

    def draw_circle_in_middle(self, widget, color):
        middle_circle = widget.addEllipse(100, 100, 200, 200, QPen(QColor("#FFFFFF"), 5), QBrush(color))
        middle_circle.setZValue(100)

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
        self.draw_sector(self.scene, start_angle, end_angle1, QColor("#77AE7D"))

        # Desenha o segundo setor
        self.draw_sector(self.scene, end_angle1, end_angle2, QColor("#e74c3c"))

        # Desenha um circulo no meio
        self.draw_circle_in_middle(self.scene, QColor("#232327"))
