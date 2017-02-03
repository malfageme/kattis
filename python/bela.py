import sys

line=sys.stdin.readline().split()
num_hands=int(line[0])
dominant=line[1]

score={
        'A':(11,11),
        'K':(4,4),
        'Q':(3,3),
        'J':(20,2),
        'T':(10,10),
        '9':(14,0),
        '8':(0,0),
        '7':(0,0),
      }


total=0
for line in sys.stdin:
    total+=score[line[0]][0] if line[1]==dominant else score[line[0]][1]


print total
