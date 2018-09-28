from montecarlo import MonteCarlo
from node import Node
import jsonpickle

algo = MonteCarlo()
algo.simulate(10)

root = Node()
child1 = Node()
child2=Node()
child3=Node()
child21=Node()
root.setExplored()
child1.setExplored()
child2.setExplored()
child2.addChild(child21)
root.addChild(child1)
root.addChild(child2)
root.addChild(child3)

frozen = jsonpickle.encode(root)
print(root.toString())
print("\n ------------------------------------------------------------ \n")
print(frozen)

file = open("save.txt",'w')
file.write(frozen)
file.close()

file=open("save.txt",'r')
thawed=jsonpickle.decode(file.read())
print("\n ----------------------BLARGH---------------------------- \n")
print(thawed)
print("\n ----------------------BLEH---------------------------- \n")
print(thawed.toString())
