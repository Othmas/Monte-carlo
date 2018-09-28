class Node(object):
    score = 0
    index = 0
    passCount = 0
    children = []
    explored = False
    
    def __init__(self, index):
        self.index = index

    def addChild(self, child):
        self.children.append(child)

    def getChild(self, index):
        return self.children[index]

    def setScore(self, newScore):
        self.score = newScore

    def getScore(self):
        return self.score
    
    def setPassCount(self, newPassCount):
        self.passCount = newPassCount

    def getPassCount(self):
        return self.passCount

    def getChildCount(self):
        return self.children.count()

    def getChildren(self):
        return self.children

    def getIndex(self):
        return self.index

    def isExplored(self):
        return self.explored

    def setExplored(self):
        self.explored = True