#!/usr/bin/python

import sys

board=[]
moves=[(0,-1),(-1,0),(0,1),(1,0)]

def reverse_rows(board):
    for i in range(len(board)):
        board[i]=board[i][::-1]
    return board


for i in range(4):
    board.append(map(int, sys.stdin.readline().split()))

move=int(sys.stdin.readline())


if move==0:
    pass
elif move==1:
    board=zip(*board)
elif move==2:
    board=reverse_rows(board)
elif move==3:
    board=zip(*board)
    board=reverse_rows(board)

for i in range(len(board)):
    board[i]=[x for x in board[i] if x!=0]
    board[i]+=[0]*(4-len(board[i]))
    for j in range(len(board[i])-1):
        if board[i][j]!=0 and board[i][j]==board[i][j+1]:
            board[i][j]*=2
            board[i][j+1]=0
    board[i]=[x for x in board[i] if x!=0]
    board[i]+=[0]*(4-len(board[i]))

if move==0:
    pass
elif move==1:
    board=zip(*board)
elif move==2:
    board=reverse_rows(board)
elif move==3:
    board=reverse_rows(board)
    board=zip(*board)

for row in board:
    print " ".join(map(str,row))


