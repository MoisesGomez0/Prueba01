class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.children = LinkedList()
class LinkedList:
    def __init__(self):
        self.first = None
#Imprime el valor de todos los nodos
    def showInColose(self):
        current = self.first
        while(current.next):
            print(current.value)
            current = current.next
        print(current.value)
#Añade un elemento al final de la lista
    def addEnd(self, value):
        if (not self.first):
            self.first = Node(value)
            return True
        else:
            current = self.first
            while(current.next):
                current = current.next
            current.next = Node(value)
            return True
#pega un nodo al final de la lista
    def addNodeEnd(self,value):
        if not self.first:
            self.first = value
            return True
        else:
            current = self.first
            while current.next:
                current = current.next
            current.next = value
            return True
        return False
#Añade un elemento al inicio de la lista
    def addFirst(self,value):
        temp = self.first
        self.first = Node(value)
        self.first.next = temp
        return True
#Retorna el primer nodo con valor igual al parámetro value
    def getListNode(self,value):
        current = self.first
        while current:
            if current.value == value:
                return current
            current = current.next
        return False
#Retorna un True si algun nodo tiene como valor el parámetro value
    def listSearch(self,value):
        current = self.first
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
#Elimina todos los nodos que tengan como valor el parámetro value
    def deleteAll(self,value):
        current = self.first
        previous = self.first
        condition = False
        if current.value == value:
            self.first = current.next
        else:
            current = current.next
            while current:
                if current.value == value:
                    previous.next = previous.next.next
                    current = previous.next
                else:
                    current = current.next
                    previous = previous.next
#Elimina el primer nodo que tenga como valor el parámetro value
    def deleteFirst(self,value):
        current = self.first
        previous = self.first
        condition = False
        if current.value == value:
            self.first = current.next
            return True
        else:
            current = current.next
            while current:
                if current.value == value:
                    previous.next = previous.next.next
                    current = previous.next
                    return True
                else:
                    current = current.next
                    previous = previous.next
        return False
#Elimina todos los nodos repetidos dejando solo el primer nodo que tenga tal valor
    def purgeSelf(self):
        test = self.first
        current = test.next
        previous = test
        while test:
            while current:
                if test.value == current.value:
                    previous.next = previous.next.next
                    current = previous.next
                else:
                    previous = previous.next
                    current = current.next
            test = test.next
            if test:
                current = test.next
                previous = test

    def purge(self):
        newList = LinkedList()
        newList.first = self.first
        test = newList.first
        current = test.next
        previous = test
        while test:

            while current:
                if test.value == current.value:
                    previous.next = previous.next.next
                    current = previous.next
                else:
                    previous = previous.next
                    current = current.next
            test = test.next
            if test:
                current = test.next
                previous = test
            else:
                return newList
#Ese método retorna el primer nodo
    def getFirst(self):
        return self.first
#Retornar el último nodo
    def getLast(self):
        temp = self.first
        while(temp.next):
            temp = temp.next
        return temp
#Añade un nodo en la posición que tenga como número el valor n
    def addInPosition(self,value,n):
        if(n == 0):
            temp = self.first
            self.first = Node(value)
            self.firt.next = temp
            return True
        elif(n>1):
            count = 0
            temp = self.first
            tempPre = self.first
            while(temp.next):
                temp = temp.next
                count+=1
                if(count == n):
                    tempPre.next = Node(value)
                    (tempPre.next).next = temp
                    return True
                tempPre = tempPre.next
        return False

#Une la linkedList que es dada como parámetro al final de la lista
    def join(self,linkedList):
        current = self.first
        while(current.next):
            current = current.next
        current.next = linkedList.first

#Esta función añade un nuevo nodo item despues del valor value
    def addAfter(self,item,value):
        current = self.first
        while current:
            if current.value == value:
                after = current.next
                current.next = Node(item)
                current.next.next = after
                return True
            else:
                current = current.next
        return False
#Esta función cuenta cuantos nodos con valor igual a value
    def count(self,value):
        counter = 0
        current = self.first
        while current:
            if current.value == value:
                counter+=1
            current = current.next
        return counter