from menu_ui import *
from PyQt5.QtGui import QIcon

class MainWindow(QtWidgets.QMainWindow,Ui_Menu):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add)
#El objeto boton se llama pushButton
#cuando le den click se activa el evento clicked
#con connect llamo a una funcion que quiero que se ejecute
        self.pushButton.setIcon(QIcon("icono.ico"))
#Con setIcon Configuto el icono del objeto
        self.listWidget.itemDoubleClicked.connect(self.labelshow)
#el objeto lista se llama listWidget y el evento itemDoubleClicked es cuando el usuario hacer doble clik en un item
    def labelshow(self):
        self.label.setText(self.listWidget.currentItem().text())
#Con esta funcion cambio el texto de un label con setText, y el argumento de esta funcion es una funcion de la lista que te devuelte el item que esta siendo seleccionedo y este tiene una propiedad .text que es el texto que este contiene
    def add(self):
        item = QtWidgets.QListWidgetItem(QIcon("world.ico"),self.lineEdit.displayText())
#cre un objeto de tipo QListWidgetItem el primet parametro para este es un icono, el segunto es una fucion de la caja de texto que se llama lineEdit que te devuelte el texto que esta contiene
        self.listWidget.addItem(item)
#Agrego el item a la lista
        self.lineEdit.setText("")
#borro el texto que esta en la caja

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

