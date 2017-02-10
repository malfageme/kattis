import sys

num_targets=int(sys.stdin.readline())

targets=[]
for _ in range(num_targets):
    targets.append(sys.stdin.readline().split())
    targets[-1]=[targets[-1][0]]+map(int,targets[-1][1:])


def calc_shot(x,y,target):
    if target[0]=='circle':
        distance=(((target[1]-x)**2)+((target[2]-y)**2))**(1.0/2)
        return distance<=target[3]
    else:
        return x>=target[1] and x<=target[3] and y>=target[2] and y<=target[4]


num_shots=int(sys.stdin.readline())
for _ in range(num_shots):
    x,y=map(int,sys.stdin.readline().split())
    print [calc_shot(x,y,target) for target in targets].count(True)
