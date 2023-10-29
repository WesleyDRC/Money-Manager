# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'header.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_header(object):
    def setupUi(self, header):
        header.setObjectName("header")
        header.resize(534, 110)
        header.setMaximumSize(QtCore.QSize(16777215, 110))
        header.setAutoFillBackground(False)
        header.setStyleSheet("#header\n"
"{\n"
"    background-color: #2E2E33;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(header)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_logo = QtWidgets.QLabel(header)
        self.lb_logo.setMaximumSize(QtCore.QSize(120, 70))
        self.lb_logo.setText("")
        self.lb_logo.setPixmap(QtGui.QPixmap(":/header/logo"))
        self.lb_logo.setScaledContents(True)
        self.lb_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_logo.setObjectName("lb_logo")
        self.horizontalLayout.addWidget(self.lb_logo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(header)
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/header/close"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.retranslateUi(header)
        QtCore.QMetaObject.connectSlotsByName(header)

    def retranslateUi(self, header):
        _translate = QtCore.QCoreApplication.translate
        header.setWindowTitle(_translate("header", "Form"))
import src.resource.resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    header = QtWidgets.QWidget()
    ui = Ui_header()
    ui.setupUi(header)
    header.show()
    sys.exit(app.exec_())