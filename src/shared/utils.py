from typing import Union

from PyQt5 import QtWidgets as QtW

class Utils:
    @staticmethod
    def clear_layout(self, layout: Union[QtW.QVBoxLayout, QtW.QHBoxLayout]):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            layout_next = item.layout()

            if(widget):
                print("has widget")
                widget.hide()
            elif(layout):
                self.clear_layout(layout_next)
