import sys

num_points=int(sys.stdin.readline())

def dist(i,j):
    return int(0.5+((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**(1.0/2))
    #return int(0.5+((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2))

def calc_distances():
    d=[[[0] for i in range(num_points)] for j in range(num_points)]
    for i in range(num_points):
        for j in range(num_points):
            d[i][j]=dist(i,j)
            d[j][i]=d[i][j]
    return d



def GreedyTour(initial=0):
    tour=[initial]
    used=[False]*num_points
    used[initial]=True
    dist_travel=0
    for i in range(1,num_points):
        best=-1
        for j in range(num_points):
            #if not used[j] and (best==-1 or dist(tour[i-1],j) < dist(tour[i-1],best)):
            if not used[j] and (best==-1 or dist_matrix[tour[i-1]][j] < dist_matrix[tour[i-1]][best]):
                best=j
        tour.append(best)
        used[best]=True
        dist_travel+=dist_matrix[tour[i-1]][best]
        #print "Distance between {} and {}".format(tour[i-1],best)
    dist_travel+=dist_matrix[tour[-1]][tour[0]]
    return tour,dist_travel

points=[]
for i in range(num_points):
    x,y=map(float, sys.stdin.readline().split())
    points.append((x,y))

dist_matrix=calc_distances()
#print dist_matrix

min_tour=[]
min_len=None
#for i in range(0,num_points,4):
for i in range(1):
    tour,d=GreedyTour(i)
    #print tour,d
    if not min_len or d<min_len:
        min_tour=tour
        min_len=d

for p in min_tour:
    print p

#print min_tour, min_len
