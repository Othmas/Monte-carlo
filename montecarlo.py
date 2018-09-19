from node import Node

class MonteCarlo(object):
    baseTree = []
    researchTree = []

    def setBaseTree(self, newBaseTree):
        self.baseTree = newBaseTree

    def setReasearchTree(self, newResearchTree):
        self.researchTree = newResearchTree

    def getResearchTree(self):
        return self.researchTree

    def isTotallyExplored(self):
        if self.baseTree.count == self.researchTree.count:
            return True
        else:
            return False

    def simulate(self, count):
        if count == 0 or self.isTotallyExplored():
            return

        self.descent()
        self.growth()
        self.rollOut()
        self.update()

    def descent(self):
        print("descent")

    def growth(self):
        print("growth")

    def rollOut(self):
        print("rollOut")

    def update(self):
        print("update")

    