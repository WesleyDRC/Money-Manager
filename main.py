from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget
import sys

from src.templates.home.home import Ui_header 

class MrMoneyManager(QMainWindow):
    def __init__(self, app):
        super(MrMoneyManager, self).__init__()
        self.app = app
        self.initUI()
        

    
        
    def initUI(self):
        self.width = self.app.desktop().screenGeometry().width()
        self.height = self.app.desktop().screenGeometry().height()
        self.setGeometry(0, 0, self.width, self.height)
        
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
        
        # Instanciar QWidgets
        self.widget_ui_core = QWidget(self)
        self.widget_ui_footer = QWidget(self)
        
        # Instanciar interfaces .ui
        self.initHeader()
        self.initCore()
        self.initFooter()
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
        self.widget_ui_core.setStyleSheet("background-color: #FFFFFF ")

    def initFooter(self):
        self.widget_ui_footer.setStyleSheet("background-color: #000000 ")
        self.widget_ui_footer.setMaximumHeight(60)
        
    def addInterfacesInLayouts(self):
        self.header_layout.addWidget(self.widget_ui_header)
        self.core_content_layout.addWidget(self.widget_ui_core)
        self.footer_layout.addWidget(self.widget_ui_footer)
        

def window():
    app = QApplication(sys.argv)
    
    win = MrMoneyManager(app)
    
    win.show()
    sys.exit(app.exec_())
    
window()
