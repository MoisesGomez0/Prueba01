# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 521)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(900, 521))
        Form.setMaximumSize(QtCore.QSize(900, 521))
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Explorer1 = QtWidgets.QListWidget(Form)
        self.Explorer1.setGeometry(QtCore.QRect(100, 40, 256, 361))
        self.Explorer1.setObjectName("Explorer1")
        self.Explorer2 = QtWidgets.QListWidget(Form)
        self.Explorer2.setGeometry(QtCore.QRect(550, 40, 260, 361))
        self.Explorer2.setObjectName("Explorer2")
        self.NDir1 = QtWidgets.QPushButton(Form)
        self.NDir1.setGeometry(QtCore.QRect(211, 410, 50, 50))
        self.NDir1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("newFolder.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NDir1.setIcon(icon)
        self.NDir1.setIconSize(QtCore.QSize(20, 20))
        self.NDir1.setObjectName("NDir1")
        self.Delete1 = QtWidgets.QPushButton(Form)
        self.Delete1.setGeometry(QtCore.QRect(290, 410, 50, 50))
        self.Delete1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("trash.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Delete1.setIcon(icon1)
        self.Delete1.setIconSize(QtCore.QSize(20, 20))
        self.Delete1.setObjectName("Delete1")
        self.NDir2 = QtWidgets.QPushButton(Form)
        self.NDir2.setGeometry(QtCore.QRect(651, 410, 50, 50))
        self.NDir2.setText("")
        self.NDir2.setIcon(icon)
        self.NDir2.setIconSize(QtCore.QSize(20, 20))
        self.NDir2.setObjectName("NDir2")
        self.DFile1 = QtWidgets.QPushButton(Form)
        self.DFile1.setGeometry(QtCore.QRect(570, 410, 50, 50))
        self.DFile1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("newFile.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DFile1.setIcon(icon2)
        self.DFile1.setIconSize(QtCore.QSize(20, 20))
        self.DFile1.setObjectName("DFile1")
        self.Delete2 = QtWidgets.QPushButton(Form)
        self.Delete2.setGeometry(QtCore.QRect(740, 410, 50, 50))
        self.Delete2.setText("")
        self.Delete2.setIcon(icon1)
        self.Delete2.setIconSize(QtCore.QSize(20, 20))
        self.Delete2.setObjectName("Delete2")
        self.Of1To2 = QtWidgets.QPushButton(Form)
        self.Of1To2.setGeometry(QtCore.QRect(400, 160, 91, 31))
        self.Of1To2.setObjectName("Of1To2")
        self.Of2To1 = QtWidgets.QPushButton(Form)
        self.Of2To1.setGeometry(QtCore.QRect(400, 220, 91, 31))
        self.Of2To1.setObjectName("Of2To1")
        self.NFile1 = QtWidgets.QPushButton(Form)
        self.NFile1.setGeometry(QtCore.QRect(130, 410, 50, 50))
        self.NFile1.setText("")
        self.NFile1.setIcon(icon2)
        self.NFile1.setIconSize(QtCore.QSize(20, 20))
        self.NFile1.setObjectName("NFile1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Directorios"))
        self.Of1To2.setText(_translate("Form", "----->"))
        self.Of2To1.setText(_translate("Form", "<-----"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
