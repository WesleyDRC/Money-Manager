from PyQt5.QtWidgets import QApplication
import sys

# Interfaces .UI
from src.templates.header.header import Ui_header
from src.templates.footer.footer import Ui_footer
from src.templates.core.components.limitAndExpense.limit_and_expense import Ui_limitAndExpense

from src.views.main.view import MainView
from src.controllers.main.controller import MainController

from src.shared.parameters import Parameters

# class MrMoneyManager(QMainWindow):
#     def __init__(self, app):
#         super(MrMoneyManager, self).__init__()
#         self.app = app
#         self.initUI()

#     def initUI(self):
#         self.width = self.app.desktop().screenGeometry().width()
#         self.height = self.app.desktop().screenGeometry().height()
#         self.setGeometry(0, 0, self.width, self.height)
#         self.setMinimumSize(1024,768)

#         # Inicialize o aplicativo em tela cheia
#         self.showMaximized()

#         # Estilizar interface
#         self.setObjectName("body")
#         self.setWindowTitle("MR Manager")
#         self.setStyleSheet("#body {background-color: #232327}")

#         # Instanciar layouts das interfaces
#         self.main_layout = QVBoxLayout()
#         self.header_layout = QHBoxLayout()
#         self.core_content_layout = QVBoxLayout()
#         self.footer_layout = QHBoxLayout()

#         # Instanciar interfaces .ui
#         self.initHeader()
#         self.initFooter()
#         self.initCore()

#         self.initMain()

#         # Inserir interfaces .ui em seus devidos layouts
#         self.addInterfacesInLayouts()

#         main_widget = QWidget()
#         main_widget.setLayout(self.main_layout)
#         self.setCentralWidget(main_widget)

#     def initMain(self):
#         self.main_layout.setSpacing(0)
#         self.main_layout.setContentsMargins(0,0,0,0)
#         self.main_layout.addLayout(self.header_layout)
#         self.main_layout.addLayout(self.core_content_layout)
#         self.main_layout.addLayout(self.footer_layout)

#     def initHeader(self):
#         self.widget_ui_header = QWidget(self)

#         self.ui_header = Ui_header()
#         self.ui_header.setupUi(self.widget_ui_header)
#         self.widget_ui_header.setMaximumHeight(60)

#     def initCore(self):
#         self.widget_ui_core = QWidget(self)
#         self.widget_ui_core.setMaximumWidth(self.width)
#         self.widget_ui_core.setMaximumHeight(self.height - self.widget_ui_header.height() - self.widget_ui_footer.height())

#         self.widget_ui_core.setObjectName("core")
#         self.widget_ui_core.setStyleSheet("#core {background-color: #232327}" )

#         # CHART
#         # Essa eh a cena onde inserimos os componentes/itens
#         self.scene = QGraphicsScene()
#         # Widget que exibe a cena
#         self.view = QGraphicsView(self.scene)

#         self.view.setObjectName("circle")
#         self.view.setStyleSheet("#circle {background-color: #232327; border: none}")

#         value1 = 0.9
#         value2 = 0.1

#         # Angulo inicial e final dos setores
#         start_angle = 0
#         end_angle1 = 360 * value1
#         end_angle2 = 360 * (value1 + value2)

#         # Desenha o primeiro setor
#         self.draw_sector(self.scene, start_angle, end_angle1, QColor("#77AE7D"))

#         # Desenha o segundo setor
#         self.draw_sector(self.scene, end_angle1, end_angle2, QColor("#e74c3c"))

#         # Desenha um círculo no meio
#         self.draw_circle_in_middle(self.scene, QColor("#232327"))

#         self.layout_widget_ui_core = QHBoxLayout(self.widget_ui_core)

#         self.layout_widgets_limits_and_chart = QVBoxLayout()
#         self.layout_widget_ui_core.addStretch()
#         self.layout_widget_ui_core.addLayout(self.layout_widgets_limits_and_chart)
#         self.layout_widget_ui_core.addStretch()

#         self.widget_ui_limit_and_expense = QWidget(self)
#         self.ui_limit_and_expense = Ui_limitAndExpense()
#         self.ui_limit_and_expense.setupUi(self.widget_ui_limit_and_expense)

#         self.layout_widgets_limits_and_chart.addStretch()
#         self.layout_widgets_limits_and_chart.addWidget(self.widget_ui_limit_and_expense)
#         self.layout_widgets_limits_and_chart.addWidget(self.view)
#         self.layout_widgets_limits_and_chart.addStretch()

#     def initFooter(self):
#         self.widget_ui_footer = QWidget(self)
#         self.ui_footer = Ui_footer()
#         self.ui_footer.setupUi(self.widget_ui_footer)
#         self.widget_ui_footer.setMaximumHeight(60)

#     def addInterfacesInLayouts(self):
#         self.header_layout.addWidget(self.widget_ui_header)
#         self.core_content_layout.addWidget(self.widget_ui_core)
#         self.footer_layout.addWidget(self.widget_ui_footer)

#     def resizeEvent(self, event):
#         # Atualize o tamanho do widget com base no tamanho da janela
#         self.width = event.size().width()
#         self.height = event.size().height()

#     def draw_sector(self, widget, start_angle, end_angle, color):
#         sector = widget.addEllipse(50, 50, 300, 300, QPen(QColor("#FFFFFF"), 5), QBrush(color))
#         sector.setStartAngle(int(start_angle * 16))
#         sector.setSpanAngle(int((end_angle - start_angle) * 16))

#     def draw_circle_in_middle(self, widget, color):
        # middle_circle = widget.addEllipse(100, 100, 200, 200, QPen(QColor("#FFFFFF"), 5), QBrush(color))
        # middle_circle.setZValue(100)

def configureParameters(app: QApplication):
    # Initializing the parameters class only once
    Parameters()

    Parameters.setScreenWidth(app.desktop().screenGeometry().width())
    Parameters.setScreenHeight(app.desktop().screenGeometry().height())

if __name__ == "__main__":
    print("Starting the application")
    app = QApplication(sys.argv)

    configureParameters(app)

    view = MainView()

    MainController(app, view)

    sys.exit(app.exec_())
