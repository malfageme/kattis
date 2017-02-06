import sys

moves=[(-1,0),(1,0),(0,-1),(0,1)]
board=[]

for line in range(7):
    board.append(sys.stdin.readline())

total_moves=0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j]=="o":
            for move in moves:
                if i+2*move[0]>=0 and i+2*move[0]<len(board) and j+2*move[1]>=0 and j+2*move[1]<len(board[i]):
                    if board[i+move[0]][j+move[1]] == "o" and board[i+2*move[0]][j+2*move[1]] == ".":
                        total_moves+=1

print total_moves

