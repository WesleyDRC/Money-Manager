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
    self.header_ui.setupUi(self.header_widget)

    self.content_widget = QtW.QWidget(self.main_view)

    self.footer_widget = QtW.QWidget(self.main_view)
    self.footer_ui = Ui_footer()
    self.footer_ui.setupUi(self.footer_widget)

    self.configure_interface()

  def configure_interface(self):
    self.layout_all_ui()
    self.configure_layout()

  def layout_all_ui(self):
    self.lt_header = QtW.QVBoxLayout()
    self.lt_header.addWidget(self.header_widget)

    self.lt_content = QtW.QVBoxLayout()
    self.lt_content.addWidget(self.content_widget)

    self.lt_footer = QtW.QVBoxLayout()
    self.lt_footer.addWidget(self.footer_widget)

    self.main_view.main_layout.addLayout(self.lt_header)
    self.main_view.main_layout.addLayout(self.lt_content)
    self.main_view.main_layout.addLayout(self.lt_footer)


  def configure_layout(self):
    #self.header_widget.move(0,0)
    print(Parameters.getScreenWidth())

    #self.header_widget.setSizePolicy(QtW.QSizePolicy.Expanding, QtW.QSizePolicy.Expanding)

    #self.footer_widget.move(0, self.main_view.height())
    self.main_view.showMaximized()
