from PyQt5.QtWidgets import QApplication
import sys

# Interfaces .UI

from src.views.main.view import MainView
from src.controllers.main.controller import MainController

from src.shared.parameters import Parameters

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
