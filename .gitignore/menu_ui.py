# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(590, 348)
        self.centralWidget = QtWidgets.QWidget(Menu)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(300, 20, 271, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 240, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 256, 271))
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 180, 191, 25))
        self.lineEdit.setObjectName("lineEdit")
        Menu.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Menu)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 590, 22))
        self.menuBar.setObjectName("menuBar")
        Menu.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Menu)
        self.mainToolBar.setObjectName("mainToolBar")
        Menu.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Menu)
        self.statusBar.setObjectName("statusBar")
        Menu.setStatusBar(self.statusBar)

        self.retranslateUi(Menu)
        self.listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.pushButton.setText(_translate("Menu", "Agregar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())
