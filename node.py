class Node(object):
    score = 0
    passCount = 0
    children = []
    explored = False
    
    def addChild(self, child):
        self.children.append(child)

    def getChild(self, index):
        return self.children[index]

    def setScore(self, newScore):
        self.score = newScore
    
    def setPassCount(self, newPassCount):
        self.passCount = newPassCount

    def getChildCount(self):
        return self.children.count()

    def isExplored(self):
        return self.explored

    def setExplored(self):
        self.explored = True