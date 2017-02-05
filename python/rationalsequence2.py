import sys

num_cases=int(sys.stdin.readline())

for _ in range(num_cases):
    l=sys.stdin.readline().split()
    i=int(l[0])
    n=int(l[1].split('/')[0])
    d=int(l[1].split('/')[1])

    # Calculate the path taken to reach the node
    n1,n2=n,d
    path=""
    while n1!=n2:
        if n1<n2:
            path='L'+path
            n2-=n1
        else:
            path='R'+path
            n1-=n2

    # Count the nodes traversed when each edge of the graph is taken
    nodes_traversed=1
    for edge in path:
        if edge=="L":
            nodes_traversed=2*nodes_traversed
        else:
            nodes_traversed=2*nodes_traversed+1

    print "{} {}".format(i,nodes_traversed)


