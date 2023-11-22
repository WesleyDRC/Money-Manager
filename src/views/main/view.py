from PyQt5.QtWidgets import QMainWindow

from src.shared.definitions import APPLICATION_WINDOW_TITLE

from src.shared.parameters import Parameters

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_UI()

    def init_UI(self):
        self.setWindowTitle(APPLICATION_WINDOW_TITLE)
        self.setMinimumSize(1024,768)

        # Estilizar interface
        self.setObjectName("body")
        self.setStyleSheet("#body {background-color: #232327}")

    def resizeEvent(self, event):
        # Atualize o tamanho do widget com base no tamanho da janela
        Parameters.setScreenWidth(event.size().width())
        Parameters.setScreenHeight(event.size().height())

        
