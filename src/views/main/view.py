from PyQt5 import QtWidgets as QtW

from src.shared.definitions import APPLICATION_WINDOW_TITLE

from src.shared.parameters import Parameters

class MainView(QtW.QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_widget = QtW.QWidget()
        self.main_layout = QtW.QVBoxLayout()

        self.init_UI()

    def init_UI(self):
        self.setWindowTitle(APPLICATION_WINDOW_TITLE)
        self.setMinimumSize(1024,768)

        # Estilizar interface
        self.setObjectName("body")
        self.setStyleSheet("#body {background-color: #232327}")
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0,0,0,0)

        self.btn_teste = QtW.QPushButton(self.main_widget)
        self.btn_teste.setText("Button1")

                # Adicione o botão ao layout
        self.main_layout.addWidget(self.btn_teste)

        self.btn_teste.clicked.connect(self.receber_sinal)


        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

    def resizeEvent(self, event):
        # Atualize o tamanho do widget com base no tamanho da janela
        Parameters.setScreenWidth(event.size().width())
        Parameters.setScreenHeight(event.size().height())


    def receber_sinal(self):
        print("Teste")
