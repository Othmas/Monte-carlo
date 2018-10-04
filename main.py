from montecarlo import MonteCarlo
from node import Node
import jsonpickle

#pip install -U jsonpickle



file=open("save.txt",'r')
thawed=jsonpickle.decode(file.read())
print(thawed.toString())

algo = MonteCarlo(thawed, None)
#algo.simulate(1)
print(algo.getNodeCount(algo.baseTree, 0))