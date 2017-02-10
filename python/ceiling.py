import sys


class Tree:

    def __init__(self):
        self.root=None

    def addNode(self, node, value):
        if not node:
            self.root=[value, None, None]
        else:
            if value<node[0]:
                if not node[1]:
                    node[1]=[value, None, None]
                else:
                    self.addNode(node[1],value)
            else:
                if not node[2]:
                    node[2]=[value, None, None]
                else:
                    self.addNode(node[2],value)

    def __str__(self):
        return str(self.root)
                

####################################################

num_prototypes, num_nodes=map(int,sys.stdin.readline().split())
topologies=set([])
for _ in range(num_prototypes):
    tree=Tree()
    nodes=map(int,sys.stdin.readline().split())

    for node in nodes:
        tree.addNode(tree.root, node)

    t="".join([x for x in str(tree) if x not in '0123456789'])
    topologies.add(t)

print len(topologies)

