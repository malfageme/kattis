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

def find_next_cell(N, holes_pos, pos):
    for j in range(pos[1]+1,N):
        if (pos[0],j) not in holes_pos:
            return(pos[0],j)
    for i in range(pos[0]+1,N):
        for j in range(0,N):
            if (i,j) not in holes_pos:
                return (i,j)
    return None

def calc_queen_solution(N, holes_pos, queens_pos, current_pos, queen=False):

    if current_pos in holes_pos:
        next_cell=find_next_cell(N, holes_pos, current_pos)
        return 0
    if check_queens(N, queens_pos+current_post[]):
        #print "Solution invalid:", queens_pos
        return 0
    elif len(queens_pos)+1==N:
        #print queens_pos
        return 1

    #print "-------------------"
    #print " Holes_pos:", holes_pos
    #print " Queens_pos:", queens_pos
    #print " current_pos:", current_pos

    next_cell=find_next_cell(N, holes_pos, current_pos)
 
    if not next_cell:
        #print " Reached final with queens:", queens_pos, current_pos
        return 0
 
    #print " Next cell:", next_cell
    next_empty_cell=find_next_cell(N, holes_pos(current_pos[0]+1, -1)
    result_with_queen=calc_queen_solution(N, holes_pos, queens_pos+[current_pos], next_empty_cell)
    #print "Result with queen:", result_with_queen
    result_without_queen=calc_queen_solution(N, holes_pos, queens_pos, )
    #print "Result without queen:", result_without_queen
    return result_with_queen + result_without_queen
        

holes_pos=[]
while 1:
    line=sys.stdin.readline().strip()
    if not line:
        break
    N, M=map(int, line.split())
    if N==0 and M==0:
        break
    holes_pos=[]
    for num_hole in range(M):
        holes_pos.append(map(int,sys.stdin.readline().split()))
    first_cell=find_next_cell(N,holes_pos,(0,-1))
    if not first_cell:
        result=0
    else:
        queens_pos=[first_cell]
        result_with=calc_queen_solution(N, holes_pos, queens_pos, first_cell)
        result_without=calc_queen_solution(N, holes_pos, [], first_cell)

    print result_with + result_without



