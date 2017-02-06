import sys

k=int(sys.stdin.readline())

num_questions=int(sys.stdin.readline())

max_time=210
current_player=k-1
current_time=0
for line in sys.stdin:
    t,z=line.split()
    t=int(t)
    if current_time+t>=max_time:
        print current_player+1
        break
    if z=='T':
        current_player=(current_player+1)%8
    current_time+=t

    
