import sys

mx=100
my=75

'''
def mix_cuts(cuts,max_len):
    new_cuts=[]
    for i in range(len(cuts)):
        gen=(x for x in range(len(cuts)) if x!=i)
        #for j in range(len(cuts)) if j!=i:
        for j in gen:
            if cuts[i][0]>=cuts[j][0] and cuts[i][0]<=cuts[j][1]:
                new_cuts=[(cuts[j][0],cuts[i][1])] + [cuts[x] for x in range(len(cuts)) if  x!=i and x!=j]
                return mix_cuts(new_cuts,max_len)
            elif cuts[i][1]>=cuts[j][0] and cuts[i][1]<=cuts[j][1]:
                new_cuts=[(cuts[i][0],cuts[j][1])] + [cuts[x] for x in range(len(cuts)) if  x!=i and x!=j]
                return mix_cuts(new_cuts,max_len)
    return cuts
'''

def check_line(cuts, w):
    for j in range(0,len(cuts)-1):
        if cuts[j+1]-cuts[j]>w:
            return False
    return True

while True:
    nx,ny,w=map(float,sys.stdin.readline().split())
    if nx==ny==w==0:
        break
    py=sorted(map(float,sys.stdin.readline().split()))
    px=sorted(map(float,sys.stdin.readline().split()))

    py=[(0-w/2)]+py+[(my+w/2)]
    px=[(0-w/2)]+px+[(mx+w/2)]

    print 'YES' if check_line(py,w) and check_line(px,w) else 'NO'

