#!/usr/bin/python

import sys
from operator import itemgetter

def check_queen(N, queen_pos, queens_pos):
    pass

def check_queens(N, queen_pos_list):
    for pos in queen_pos_list:
        x,y=pos
        # Hor
        if [p[0] for p in queen_pos_list].count(x) > 1:
            return True
        # Ver
        if [p[1] for p in queen_pos_list].count(x) > 1:
            return True
        # Diag from top-left to bottom-right
        diag1_pos=[]
        updated=False
        for i in range(1,N):
            updated=False
            if x-i >= 0 and y-i >= 0:
                diag1_pos.append((x-i,y-i))
                updated=True
            if x+i < N and y+i < N:
                diag1_pos.append((x+i,y+i))
                updated=True
            if not updated:
                break
        if len([p for p in queen_pos_list if p in diag1_pos])>0:
            return True
        #print "Diag 1 for pos: ", pos, diag1_pos
        # Diag from bottom-left to top-right
        diag2_pos=[]
        updated=False
        for i in range(1,N):
            updated=False
            if x-i >= 0 and y+i < N:
                diag2_pos.append((x-i,y+i))
                updated=True
            if x+i < N and y-i >=0:
                diag2_pos.append((x+i,y-i))
                updated=True
            if not updated:
                break
        #print "Diag 2 for pos: ", pos, diag2_pos
        if len([p for p in queen_pos_list if p in diag2_pos])>0:
            return True
 
queens_pos=[]
num_line=0
for line in sys.stdin:
    line=line.strip()
    for i in range(len(line)):
        if line[i]=='*':
            queens_pos.append((num_line,i))
    num_line+=1
N=num_line

print 'invalid' if len(queens_pos) != 8 or check_queens(N, queens_pos) else 'valid'


