from form_ui import *
from Tree import *
from PyQt5.QtGui import QIcon

class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.tree1 = TSVToTree("Archivo.tsv")
        self.tree2 = TSVToTree("Archivo2.tsv")
        self.parent1 = self.tree1.root.value
        self.parent2 = self.tree2.root.value
        self.showInExplorer(self.tree1.showChilds(self.tree1.root.value),self.Explorer1)
        self.showInExplorer(self.tree2.showChilds(self.tree2.root.value),self.Explorer2)
        self.center()
        self.Explorer1.itemDoubleClicked.connect(self.changeDir1)
        self.Explorer2.itemDoubleClicked.connect(self.changeDir2)
        self.Delete1.clicked.connect(self.remove1)
        self.Delete2.clicked.connect(self.remove2)
    def remove1(self):
        value = self.Explorer1.currentItem().text()
        if not value or value == "." or value == "..": return False
        dialog = QtWidgets.QMessageBox.question(self,"Advertencia","Desea eliminar a: %s"%value)
        answer = dialog==QtWidgets.QMessageBox.StandardButtons(QtWidgets.QMessageBox.Yes)
        if answer:
            if value == self.tree1.root.value and not self.parent1:
                self.tree1.delete(value,self.parent1)
                self.tree1.TreeNodeToFileTSV(self.tree1.root,"Archivo.tsv")
                self.Explorer1.clear()
            if self.tree1.delete(value,self.parent1):
                self.tree1.TreeNodeToFileTSV(self.tree1.root,"Archivo.tsv")
                self.Explorer1.clear()
                self.showInExplorer(self.tree1.showChilds(self.parent1),self.Explorer1)
                return True
        else: return False
    def remove2(self):
        value = self.Explorer2.currentItem().text()
        if not value or value == "." or value == "..": return False
        dialog = QtWidgets.QMessageBox.question(self,"Advertencia","Desea eliminar a: %s"%value)
        answer = dialog==QtWidgets.QMessageBox.StandardButtons(QtWidgets.QMessageBox.Yes)
        if answer:
            if value == self.tree2.root.value and not self.parent2:
                self.tree2.delete(value,self.parent2)
                self.tree2.TreeNodeToFileTSV(self.tree2.root,"Archivo2.tsv")
                self.Explorer2.clear()
            if self.tree2.delete(value,self.parent2):
                self.tree2.TreeNodeToFileTSV(self.tree2.root,"Archivo2.tsv")
                self.Explorer2.clear()
                self.showInExplorer(self.tree2.showChilds(self.parent2),self.Explorer2)
                return True
        else: return False
    def changeDir1(self):
        name = self.Explorer1.currentItem().text()
        if name[len(name)-1:] == "/":
            self.Explorer1.clear()
            array = self.tree1.showChilds(name)
            self.showInExplorer(array,self.Explorer1)
            self.parent1 = name
        elif name == "..":
            parent = self.tree1.showParent(self.parent1)
            if parent:
                self.Explorer1.clear()
                parent = parent.value
                self.showInExplorer(self.tree1.showChilds(parent),self.Explorer1)
                self.parent1 = parent
            elif self.parent1 == self.tree1.root.value:
                self.Explorer1.clear()
                item = QtWidgets.QListWidgetItem(QIcon("folder.ico"),self.parent1)
                self.Explorer1.addItem(item)
                self.parent1 = None
                
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Archivo %s" %name)
            msgBox.setWindowTitle("Visor de Archivos")
            msgBox.exec()
    def changeDir2(self):
        name = self.Explorer2.currentItem().text()
        if name[len(name)-1:] == "/":
            self.Explorer2.clear()
            array = self.tree2.showChilds(name)
            self.showInExplorer(array,self.Explorer2)
            self.parent2 = name
        elif name == "..":
            parent = self.tree2.showParent(self.parent2)
            if parent:
                self.Explorer2.clear()
                parent = parent.value
                self.showInExplorer(self.tree2.showChilds(parent),self.Explorer2)
                self.parent2 = parent
            elif self.parent2 == self.tree2.root.value:
                self.Explorer2.clear()
                item = QtWidgets.QListWidgetItem(QIcon("folder.ico"),self.parent2)
                self.Explorer2.addItem(item)
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Archivo %s" %name)
            msgBox.setWindowTitle("Visor de Archivos")
            msgBox.exec()
    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        print(centerPoint)
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())    
    def showInExplorer(self,array,explorer):
        explorer.addItem(".")
        explorer.addItem("..")
        for i in array:
            if i.value[len(i.value)-1:] == "/":
                item = QtWidgets.QListWidgetItem(QIcon("folder.ico"),i.value)
                explorer.addItem(item)
            else:
                item = QtWidgets.QListWidgetItem(QIcon("file.ico"),i.value)
                explorer.addItem(item)
if __name__ == "__main__":
    apt = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    apt.exec()