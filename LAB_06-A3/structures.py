import math

class mainStruct:
    def __init__(self):
        self.dane = []
        self.L = 0
    def testPrintDane(self):
        for i in self.dane:
            print(i.value)
            print(i.parent)
            print(i.left)
            print(i.right)
            print("\n")

    def INSERT(self, value):
        if(value - 0.5) % 1 == 0:
            self.L += 1
            temp = BST()
            temp.value = value
            temp.parent = None
            self.dane.append(temp)
            self.dane.sort(key=lambda x: x.value)
        else:
            id = -1
            idValue = math.floor(value) + 0.5
            for i in range(0, self.L):
                if self.dane[i].value == idValue:
                    id = i
                    break
            if(id == -1):
                self.L += 1
                temp2 = BST()
                idValue = math.floor(value) + 0.5
                temp2.value = idValue
                temp2.parent = None
                self.dane.append(temp2)
                self.dane.sort(key=lambda x: x.value)
                for i in range(0, self.L):
                    if self.dane[i].value == idValue:
                        id = i
                        break

            temp = BST()
            temp.value = value
            y = None
            x = self.dane[id]
            while x != None:
                y = x
                if temp.value < x.value:
                    x = x.left
                else:
                    x = x.right

            temp.parent = y
            if (y == None):
                self.dane[id] = temp
            else:
                if temp.value < y.value:
                    y.left = temp
                else:
                    y.right = temp

    def printDane(self):
        for i in self.dane:
            helpPrint(i, 0)

    def MINIMUM(self, y):
        id = 0
        idValue = math.floor(y) + 0.5
        for i in range(0, self.L):
            if self.dane[i].value == idValue:
                id = i
                break
        helpMin(self.dane[id])
        return minValue
        #print(minValue)

    def MAXIMUM(self, y):
        id = 0
        idValue = math.floor(y) + 0.5
        for i in range(0, self.L):
            if self.dane[i].value == idValue:
                id = i
                break
        helpMax(self.dane[id])
        return maxValue

    def SEARCH(self, key):
        id = 0
        idValue = math.floor(key) + 0.5
        for i in range(0, self.L):
            if self.dane[i].value == idValue:
                id = i
                break
        node = self.dane[id]
        while (node != None) and (node.value != key):
            if(key < node.value):
                node = node.left
            else:
                node = node.right

        return node #if none - not found


class BST:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.parent = None


def helpPrint(abc, level):
    for a in range(0, level):
        print("-", end="")
    print(abc.value)
    if abc.left != None:
        helpPrint(abc.left, level + 1)
    if abc.right != None:
        helpPrint(abc.right, level+ 1)

minValue = 0
maxValue = 0

def helpMin(abc):
    global minValue
    if abc.left != None:
        helpMin(abc.left)
    else:
        minValue = abc.value

def helpMax(abc):
    global maxValue
    if abc.right != None:
        helpMax(abc.right)
    else:
        maxValue = abc.value
