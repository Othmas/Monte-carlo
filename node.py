class Node(object):

    def __init__(self, index):
        self.score = 0
        self.passCount = 0
        self.children = []
        self.explored = False
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
        return len(self.children)

    def getChildren(self):
        return self.children

    def getIndex(self):
        return self.index

    def isExplored(self):
        return self.explored

    def setExplored(self):
        self.explored = True

    def toString(self,increment = 0):
        i = 0
        ret ="\n"+"\t"*increment+"{\n"+"\t"*increment+"\"index\": "+str(self.index)+",\n"+"\t"*increment+"\"score\": "+str(self.score)+",\n"+"\t"*increment+"\"passcount\": "+str(self.passCount)+",\n"+"\t"*increment+"\"explored\" : "+str(self.explored)+",\n"+"\t"*increment+"\"children\": ["
        for child in self.children:
            if i >= 1:
                ret += ","
            ret += child.toString(increment + 1)
            i = i + 1
        ret +="]\n"+"\t"*increment+"}" 
        return ret