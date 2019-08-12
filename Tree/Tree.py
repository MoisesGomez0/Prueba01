from LinkedList import *
class Text:
    def __init__(self):
        self.text = ""

class Tree:
    def __init__(self):
        self.root = None
    
    def add(self,value, parent = None, current = None):
        if not self.root: 
            self.root = Node(value)
            return True
        if not parent:
            return self.root.children.addEnd(value)
        if parent == self.root.value:
            return self.root.children.addEnd(value)
        else:
            if not current:
                current = self.root
            tempNode = current.children.search(parent)
            if tempNode:
                tempNode.children.addEnd(value)
                return True
            else:
                if current.children.first:
                    tempNode = current.children.first.children.search(parent)
                    if tempNode:
                        tempNode.children.addEnd(value)
                        return True
                    else:
                        if current.children.first.next:
                            if self.add(value,parent,current.children.first.next):
                                return True
                        if current.children.first.children.first:
                            if self.add(value,parent,current.children.first.children.first):
                                return True
                elif current.next: 
                    return self.add(value,parent,current.next)
            return False
    def TreeToTSV(self,parent,count=0,text = None):
        if not text: text = Text()
        text.text+="\t"*count
        text.text+=str(parent.value)+"\n"
        if parent.next:
            if parent.children.first:
                self.TreeToTSV(parent.children.first,count+1,text)
            self.TreeToTSV(parent.next,count,text)
        elif parent.children.first:
            count+=1
            self.TreeToTSV(parent.children.first,count,text)
        return text.text
    
    def TSVToFile(self,current,filename):
        text = self.TreeToTSV(current)
        f = open(filename,"w")
        f.write(text)
        f.close
    
    def TreeSearchBool(self,value,parent=None):
        if not self.root: return False
        if not parent: parent = self.root
        if parent.value == value: return True
        if parent.children.searchBool(value): return True
        if parent.next:
            if self.TreeSearchBool(value,parent.next):
                return True
        if parent.children.first:
            if self.TreeSearchBool(value,parent.children.first):
                return True
        return False

    def TreeSearch(self,value,parent=None):
        if not self.root: return False
        if not parent: parent = self.root
        if parent.value == value: return parent
        temp = parent.children.search(value)
        if temp: return temp
        if parent.next:
            temp = self.TreeSearch(value,parent.next)
            if temp:
                return temp
        if parent.children.first:
            temp = self.TreeSearch(value,parent.children.first)
            if temp:
                return temp
        return False
    def showChilds(self,parent):
        current = self.TreeSearch(parent)
        if not current:
            return []
        elif not current.children.first:
            return []
        else:
            array = []
            current = current.children.first
            while current:
                array.append(current.value)
                current = current.next
            return array
    def showParent(self,child,parent = None):
        if not self.TreeSearchBool(child): return False
        if not parent: parent = self.root
        if parent.children.searchBool(child):
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