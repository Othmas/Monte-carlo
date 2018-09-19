from node import Node

class MonteCarlo(object):
    baseTree = []
    researchTree = []

    def setBaseTree(self, newBaseTree):
        self.baseTree = newBaseTree

    def setReasearchTree(self, newResearchTree):
        self.researchTree = newResearchTree

    def simulate(self, researchTree, count):
        if count == 0:
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

    