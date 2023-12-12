from typing import Union

from PyQt5 import QtWidgets as QtW

class Utils:
    @staticmethod
    def clear_layout(layout: Union[QtW.QVBoxLayout, QtW.QHBoxLayout], exclude_object=None):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            layout_next = item.layout()

            if(widget and widget != exclude_object):
                widget.hide()
            elif(layout_next):
                Utils.clear_layout(layout_next, exclude_object)
