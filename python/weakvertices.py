import sys

while True:
    n=int(sys.stdin.readline())
    if n==-1:
        break
    adj=[]
    for i in range(n):
        adj.append(map(int,sys.stdin.readline().split()))
    weak=[]
    for i in range(len(adj)):
        neighbours_node=[j for j in range(len(adj)) if adj[i][j]==1]
        #print "Neighbours of node {}".format(i), neighbours_node
        found=False
        for j in neighbours_node:
            neighbours_adj=[x for x in range(len(adj)) if x!=i and adj[j][x]==1]
            #print "Neighbours of the neighbour {} of node {}".format(j,i), neighbours_adj
            neigh_intersection=set.intersection(set(neighbours_node), neighbours_adj)
            #print "intersection:", neigh_intersection
            if len(set.intersection(set(neighbours_node), neighbours_adj))>0:
                break
        else:
            weak.append(i)
    print " ".join(map(str,sorted(weak)))

