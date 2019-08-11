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
                            return self.add(value,parent,current.children.first.next)
                        elif current.children.first.children.first:
                            return self.add(value,parent,current.children.first.children.first)
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