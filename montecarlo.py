from node import Node
import math 

class MonteCarlo(object):
    baseTree = []
    researchTree = []
    ponderationValue = 2
    

    def setBaseTree(self, newBaseTree):
        self.baseTree = newBaseTree

    def setReasearchTree(self, newResearchTree):
        self.researchTree = newResearchTree

    def getResearchTree(self):
        return self.researchTree

    #Si l'arbre de recherche à été complètement exploré
    def isTotallyExplored(self):
        if self.baseTree.count == self.researchTree.count:
            return True
        else:
            return False

    #Calcul l'UBC
    def calculateUBC(self, rootNode):

        selectedNode = rootNode
        currentUBC = -math.inf
        #Si tous les childrens n'ont pas été exploré, retourner le plus à gauche non exploré
        #Sinon calcul de l'Upper Bound Confidence
        for node in rootNode.getChildren:
            if node.isExplored == False:
                return node
            else :
                ubc = node.getScore + math.sqrt(self.ponderationValue*(math.log(rootNode.getPassCount() / node.getPassCount())))
                if ubc > currentUBC:
                    ubc = currentUBC
                    selectedNode = node

        return selectedNode


    #Simule de façon récursive
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

    