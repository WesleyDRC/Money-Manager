from PyQt5 import QtWidgets as QtW


from src.views.main.view import MainView

# Templates
from src.templates.header.header import Ui_header
from src.templates.footer.footer import Ui_footer

from src.shared.parameters import Parameters

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

    # Widgets Objects
    self.header_widget = None
    self.footer_widget = None

    self.main_view = view

    self.setup_ui_objects()

  def setup_ui_objects(self):
    self.header_widget = QtW.QWidget(self.main_view)
    self.header_ui = Ui_header()

    self.footer_widget = QtW.QWidget(self.main_view)
    self.footer_ui = Ui_footer()

    self.configure_interface()

  def configure_interface(self):
    self.setup_all_ui()
    self.configure_layout()

  def setup_all_ui(self):
    self.header_ui.setupUi(self.header_widget)
    self.footer_ui.setupUi(self.footer_widget)

  def configure_layout(self):
    self.header_widget.move(0,0)
    print(Parameters.getScreenWidth())
    self.header_widget.setMaximumWidth(Parameters.getScreenWidth())

    self.header_widget.setSizePolicy(QtW.QSizePolicy.Expanding, QtW.QSizePolicy.Expanding)

    self.footer_widget.move(0, self.main_view.height())
    self.main_view.showMaximized()

  def resizeEvent():
    print("tewsteee")
