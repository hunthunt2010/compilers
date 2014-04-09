
class Node:
    count = 0

    def __init__(self, name, data):
        self.name = Node.count
        Node.count += 1
        self.data = data
        #index 0 in child list = left most child
        self.children = []

    def addChild(self, newChild):
        self.children.append(newChild)

    def isLeaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def getName(self):
        return self.name

    def getData(self):
        return self.data

    def getChildren(self):
        temp = ""
        for child in self.children:
            temp += child.getName() + " "

        temp += "\n"
        for child in self.children:
            temp += child.getChildren()

        return temp