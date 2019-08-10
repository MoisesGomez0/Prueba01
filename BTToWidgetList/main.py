from form_ui import *
from Tree import *

class MainWindow(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.tree = FileTSVToTree("Archivo2.tsv")
        self.importButton.clicked.connect(self.importData)
        self.List.doubleClicked.connect(self.refreshData)

    def importData(self):
        self.List.addItem(str(self.tree.root.value))

    def refreshData(self):
        value = int(self.List.currentItem().text())
        array = self.tree.showMeChilds(int(self.List.currentItem().text()))
        self.label.setText(str(value))
        self.List.clear()
        for i in array:
            self.List.addItem(str(i))
if __name__=="__main__":
    apt = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    apt.exec_()