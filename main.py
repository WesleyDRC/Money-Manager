from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from src.templates.home.home import Ui_home 

class MrMoneyManager(QMainWindow):
    def __init__(self, app):
        super(MrMoneyManager, self).__init__()
        self.app = app
        self.initUI()
        self.width
        self.height
        
    def initUI(self):
        
        self.width = self.app.desktop().screenGeometry().width()
        self.height = self.app.desktop().screenGeometry().height()
        #self.setGeometry(0,0, self.width , self.height)
        
        # Initializing application in full screen
        self.showMaximized()
        
        self.setObjectName("body")
        
        
        self.setWindowTitle("MR Manager")
        self.setStyleSheet("#body { background-color: #232327 }")
        
        # self.widget_ui_home = QtW.QWidget(self)
        # self.ui_home = Ui_home()
        # self.ui_home.setupUi(self.widget_ui_home)
        

        
def window():
    app = QApplication(sys.argv)
    
    win = MrMoneyManager(app)
    
    win.show()
    sys.exit(app.exec_())
    
window()
