class Node:
    def __init__(self,value):
        self.left = None
        self.rigth = None
        self.value = value
class Text:
    def __init__(self):
        self.txt = ""
class Tree:
    def __init__(self):
        self.root = None

    def add(self,value,current = None):
        if not current:
            current = self.root
        if not current:
            self.root = Node(value)
            return True
        else:
            if value < current.value:
                if not current.left:
                    current.left = Node(value)
                    return True
                else:
                    return self.add(value,current.left)
            elif value > current.value:
                if not current.rigth:
                    current.rigth = Node(value)
                    return True
                else:
                    return self.add(value,current.rigth)
        return False

    def searchBool(self,value,current = None):
        if not self.root:
            return False
        if self.root and not current:
            current = self.root
        if not current:
            return False
        elif value == current.value:
            return True
        elif value > current.value:
            return self.searchBool(value,current.rigth)
        elif value < current.value:
            return self.searchBool(value,current.left)

    def TreeToTSV(self,current=None,text=None,cont = 0):
        if not text:
            text = Text()
        text.txt += str(current.value)+"\n"
        cont+=1
        if current.left:
            text.txt+="\t"*cont
            self.TreeToTSV(current.left,text,cont)
        if current.rigth:
            text.txt+="\t"*cont
            self.TreeToTSV(current.rigth,text,cont)
        return text.txt

    def TSVToFile(self,current):
        txt = self.TreeToTSV(current)
        f = open("Archivo2.tsv","w")
        f.write(txt)
        f.close()
    
    def showMeChilds(self,value,current = None):
        if not self.searchBool(value):
            return []
        else:
            array=[]
            if not current:
                current = self.root
            if value == current.value:
                if current.left:
                    array.append(current.left.value)
                if current.rigth:
                    array.append(current.rigth.value)
                return array
            elif value > current.value:
                return self.showMeChilds(value,current.rigth)
            elif value < current.value:
                return self.showMeChilds(value,current.left)

def FileTSVToTree(filename):
    f = open(filename,"r")
    content = f.read()
    bTree = Tree()
    content = content.split("\n")
    array=[]
    for i in content:
        array.append(i.split("\t"))
    for i in array:
        for j in i:
            if j !="":
                bTree.add(int(j))
    return bTree