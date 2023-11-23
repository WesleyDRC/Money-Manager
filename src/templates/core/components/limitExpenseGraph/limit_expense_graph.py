from PyQt5 import QtWidgets as QtW
from PyQt5.QtGui import QBrush, QColor, QPen

class LimitExpenseGraph:
    def draw_sector(self, widget: QtW.QGraphicsScene, start_angle, end_angle, color):
        sector = widget.addEllipse(50, 50, 300, 300, QPen(QColor("#FFFFFF"), 5), QBrush(color))
        sector.setStartAngle(int(start_angle * 16))
        sector.setSpanAngle(int((end_angle - start_angle) * 16))

    def draw_circle_in_middle(self, widget, color):
        middle_circle = widget.addEllipse(100, 100, 200, 200, QPen(QColor("#FFFFFF"), 5), QBrush(color))
        middle_circle.setZValue(100)
