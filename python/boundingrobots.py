import sys


moves_table={
                'u':(0,1),
                'd':(0,-1),
                'l':(-1,0),
                'r':(1,0)
            }

while True:
    w,l=map(int,sys.stdin.readline().split())
    if w==l==0:
        break
    dimensions=[w,l]
    fake_pos=[0,0]
    real_pos=[0,0]
    num_moves=int(sys.stdin.readline())
    for _ in range(num_moves):
        op,val=sys.stdin.readline().split()
        val=int(val)
        offset=[x*val for x in moves_table[op]]
        fake_pos=[fake_pos[i]+offset[i] for i in range(len(offset))]
        real_pos=[real_pos[i]+offset[i] for i in range(len(offset))]
        real_pos=[real_pos[i] if real_pos[i]<dimensions[i] else dimensions[i]-1 for i in range(len(offset))]
        real_pos=[real_pos[i] if real_pos[i]>0 else 0 for i in range(len(offset))]

    print "Robot thinks {} {}".format(*fake_pos)
    print "Actually at {} {}".format(*real_pos)
    print



