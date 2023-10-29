# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'footer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_footer(object):
    def setupUi(self, footer):
        footer.setObjectName("footer")
        footer.resize(400, 80)
        footer.setMaximumSize(QtCore.QSize(16777215, 80))
        footer.setStyleSheet("#footer\n"
"{\n"
"    background-color: #2E2E33\n"
"}\n"
"\n"
"#footer QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    outline: none;\n"
"}")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(footer)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_home = QtWidgets.QPushButton(footer)
        self.btn_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/footer/home_selected"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QtCore.QSize(60, 60))
        self.btn_home.setObjectName("btn_home")
        self.horizontalLayout.addWidget(self.btn_home)
        self.btn_spending = QtWidgets.QPushButton(footer)
        self.btn_spending.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_spending.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/footer/signal"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_spending.setIcon(icon1)
        self.btn_spending.setIconSize(QtCore.QSize(60, 60))
        self.btn_spending.setCheckable(False)
        self.btn_spending.setDefault(False)
        self.btn_spending.setObjectName("btn_spending")
        self.horizontalLayout.addWidget(self.btn_spending)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.retranslateUi(footer)
        QtCore.QMetaObject.connectSlotsByName(footer)

    def retranslateUi(self, footer):
        _translate = QtCore.QCoreApplication.translate
        footer.setWindowTitle(_translate("footer", "Form"))
import src.resource.resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    footer = QtWidgets.QWidget()
    ui = Ui_footer()
    ui.setupUi(footer)
    footer.show()
    sys.exit(app.exec_())