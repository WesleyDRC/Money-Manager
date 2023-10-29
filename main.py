from PyQt5.QtGui import QBrush, QColor, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QGraphicsScene, QGraphicsView
import sys

# Interfaces .UI
from src.templates.header.header import Ui_header
from src.templates.footer.footer import Ui_footer

class MrMoneyManager(QMainWindow):
    def __init__(self, app):
        super(MrMoneyManager, self).__init__()
        self.app = app
        self.initUI()

    def initUI(self):
        self.width = self.app.desktop().screenGeometry().width()
        self.height = self.app.desktop().screenGeometry().height()
        self.setGeometry(0, 0, self.width, self.height)
        self.setMinimumSize(1024,768)

        # Inicialize o aplicativo em tela cheia
        self.showMaximized()

        # Estilizar interface
        self.setObjectName("body")
        self.setWindowTitle("MR Manager")
        self.setStyleSheet("#body {background-color: #232327}")

        # Instanciar layouts das interfaces
        self.main_layout = QVBoxLayout()
        self.header_layout = QHBoxLayout()
        self.core_content_layout = QVBoxLayout()
        self.footer_layout = QHBoxLayout()

        # Instanciar interfaces .ui
        self.initHeader()
        self.initFooter()
        self.initCore()

        self.initMain()

        # Inserir interfaces .ui em seus devidos layouts
        self.addInterfacesInLayouts()

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def initMain(self):
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.addLayout(self.header_layout)
        self.main_layout.addLayout(self.core_content_layout)
        self.main_layout.addLayout(self.footer_layout)

    def initHeader(self):
        self.widget_ui_header = QWidget(self)

        self.ui_header = Ui_header()
        self.ui_header.setupUi(self.widget_ui_header)
        self.widget_ui_header.setMaximumHeight(60)

    def initCore(self):
        self.widget_ui_core = QWidget(self)
        self.widget_ui_core.setMaximumWidth(self.width)
        self.widget_ui_core.setMaximumHeight(self.height - self.widget_ui_header.height() - self.widget_ui_footer.height())

        self.widget_ui_core.setMinimumWidth(self.width)
        self.widget_ui_core.setMinimumHeight(self.height - self.widget_ui_header.height() - self.widget_ui_footer.height())

        self.widget_ui_core.setObjectName("core")
        self.widget_ui_core.setStyleSheet("#core {background-color: #232327}" )

        # Essa eh a cena onde inserimos os componentes/itens
        self.scene = QGraphicsScene()

        # Widget que exibe a cena
        self.view = QGraphicsView(self.scene)
        self.view.setObjectName("circle")
        self.view.setStyleSheet("#circle {background-color: #232327; border: none}")

        self.createSectors(self.view)

        self.view.setMinimumHeight(500)
        self.view.setMinimumWidth(500)
        self.view.setMaximumWidth(500)
        self.view.setMaximumHeight(500)

        self.view.setParent(self.widget_ui_core)

        self.width_view = int((self.widget_ui_core.width() / 2) - (self.view.width() / 2))
        self.height_view = int((self.widget_ui_core.height() / 2) - (self.view.height() / 2))

        self.view.move(self.width_view, self.height_view)

    def initFooter(self):
        self.widget_ui_footer = QWidget(self)
        self.ui_footer = Ui_footer()
        self.ui_footer.setupUi(self.widget_ui_footer)
        self.widget_ui_footer.setMaximumHeight(60)

    def addInterfacesInLayouts(self):
        self.header_layout.addWidget(self.widget_ui_header)
        self.core_content_layout.addWidget(self.widget_ui_core)
        self.footer_layout.addWidget(self.widget_ui_footer)

    def resizeEvent(self, event):
        # Atualize o tamanho do widget com base no tamanho da janela
        self.width = event.size().width()
        self.height = event.size().height()

    def createSectors(self, widget):
        value1 = 0.4
        value2 = 0.6

        # Angulo inicial e final dos setores
        start_angle = 0
        end_angle1 = 360 * value1
        end_angle2 = 360 * (value1 + value2)

        # Desenha o primeiro setor
        self.draw_sector(self.scene, start_angle, end_angle1, QColor("#77AE7D"))

        # Desenha o segundo setor
        self.draw_sector(self.scene, end_angle1, end_angle2, QColor("#e74c3c"))

        # Desenha um círculo no meio
        self.draw_circle_in_middle(self.scene, QColor("#232327"))


    def draw_sector(self, widget, start_angle, end_angle, color):
        sector = widget.addEllipse(50, 50, 300, 300, QPen(QColor("#FFFFFF"), 5), QBrush(color))
        sector.setStartAngle(int(start_angle * 16))
        sector.setSpanAngle(int((end_angle - start_angle) * 16))

    def draw_circle_in_middle(self, widget, color):
        middle_circle = widget.addEllipse(100, 100, 200, 200, QPen(QColor("#FFFFFF"), 5), QBrush(color))
        middle_circle.setZValue(100)



def window():
    app = QApplication(sys.argv)

    win = MrMoneyManager(app)

    win.show()
    sys.exit(app.exec_())

window()
