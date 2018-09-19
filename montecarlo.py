class Node(object):
    value = ""
    children = []
    
    def __init__(self, value):
        self.value = value

    def addChild(self, child):
        self.children.append(child)

def main():
    root = Node("root")

    leap1 = Node("leap1")
    leap2 = Node("leap2")

    root.addChild(leap1)
    root.addChild(leap2)

main()
    