from LinkedList import *
class Text:
    def __init__(self):
        self.text = ""

class Tree:
    def __init__(self):
        self.root = None
#Este metodo agrega un valor al arbol
    def add(self,value, parent = None):
        if not self.root: 
            self.root = Node(str(value))
            return True
        elif not parent or str(parent) == self.root.value:
            return self.root.children.addEnd(str(value))
        parent = self.getTreeNode(str(parent))
        if parent:
            return parent.children.addEnd(str(value))
        return False

#Este método convierte un Node de árbol a texto tsv, parent es un nodo de árbol
    def TreeNodeToTSV(self,parent,count=0,text = None):
        if not self.root: return ""
        if not text: text = Text()
        text.text+="\t"*count
        text.text+=str(parent.value)+"\n"
        if parent.next:
            if parent.children.first:
                self.TreeNodeToTSV(parent.children.first,count+1,text)
            self.TreeNodeToTSV(parent.next,count,text)
        elif parent.children.first:
            count+=1
            self.TreeNodeToTSV(parent.children.first,count,text)
        return text.text

#Este método converte un nodo de un arbol a un archivo tsv, current es un nodo de arbol
    def TreeNodeToFileTSV(self,current,filename):
        text = self.TreeNodeToTSV(current)
        f = open(filename,"w")
        f.write(text)
        f.close

#Esta función devuelve True si el value es el valor de un nodo en el árbol
    def treeSearch(self,value,parent=None):
        value = str(value)
        if not self.root: return False
        if not parent: parent = self.root
        if parent.value == value: return True
        if parent.children.listSearch(value): return True
        if parent.next:
            if self.treeSearch(value,parent.next):
                return True
        if parent.children.first:
            if self.treeSearch(value,parent.children.first):
                return True
        return False

#Esta función devuelve el nodo con el valor igual al value
    def getTreeNode(self,value,parent=None):
        if not self.root: return False
        if not parent: parent = self.root
        if parent.value == value: return parent
        temp = parent.children.getListNode(value)
        if temp: return temp
        if parent.next:
            temp = self.getTreeNode(value,parent.next)
            if temp:
                return temp
        if parent.children.first:
            temp = self.getTreeNode(value,parent.children.first)
            if temp:
                return temp
        return None

#Este método devuelve un arrelgo con todos los hijos que tiene el nodo con valor parent
    def showChilds(self,parent):
        current = self.getTreeNode(parent)
        if not current:
            return []
        elif not current.children.first:
            return []
        else:
            array = []
            current = current.children.first
            while current:
                array.append(current)
                current = current.next
            return array

#Añade un nodo al árbol, el parámetro node es un nodo, parent es el valor del nodo padre
    def addNode(self,node,parent= None):
        if not self.root:
            self.root = node
            return True
        if not parent:
            parent = self.root
        else:
            parent = self.getTreeNode(parent)
        if parent:
            parent.children.addNodeEnd(node)
            return True
        return False

#Este método devuelve el nodo padre del nodo que tiene valor child
    def showParent(self,child,parent = None):
        child = str(child)
        if not self.treeSearch(child):
            return False
        if not parent: 
            parent = self.root
        if parent.children.listSearch(child):
            return parent
        if parent.next:
            temp = self.showParent(child, parent.next)
            if temp:
                return temp
        if parent.children.first:
            temp = self.showParent(child, parent.children.first)
            if temp:
                return temp
        return False
    
#Este método elimina el nodo que tenga valor value y devuelve true
    def delete(self,value,parent):
        if not self.treeSearch(value): return False
        if self.root.value == value and not parent:
            self.root = None
            return True
        parent = self.getTreeNode(parent)
        return parent.children.deleteFirst(value)
        
#Este metodo devuelve un árbol desde un archivo .tsv apropiado
def TSVToTree(filename):
    f = open(filename,"r")
    content = f.read()
    content = content.split("\n")
    tree = Tree()
    tree.add(content[0].lstrip("\t"))
    for i in range(1,len(content)-1):
        parent = content[0]
        count = 1
        while parent.count("\t") != content[i].count("\t")-1:
            parent = content[count]
            count += 1
            while parent.count("\t") == content[count].count("\t"):
                parent = content[count]
                count += 1
        tree.add(content[i].lstrip("\t"),parent.lstrip("\t"))
    return tree