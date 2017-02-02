import sys

num_cases=int(sys.stdin.readline())

# Representing the movements as numbers. Each bit represent if the cell is flipped or not. LSB is top-left cell
moves=((0b000001011),
       (0b000010111),
       (0b000100110),
       (0b001011001),
       (0b010111010),
       (0b100110100),
       (0b011001000),
       (0b111010000),
       (0b110100000))


def board2int(board):
    #result=0
    #for i in range(len(board)):
    #    for j in range(len(board[i])):
    #        if board[i][j]=="*":
    #            mask=1<<(i*len(board[i])+j)
    #            result=result^mask
    #return result
    # new way
    return int("".join(board)[::-1].replace("*","1").replace(".","0"), 2)


states_viewed=[False]*512
states_moves=[None]*512

# First state
states_to_check=[0]
states_moves[0]=0
states_viewed[0]=True

# Calculate all possible states (they are only 512)
while len(states_to_check)>0:
    state=states_to_check.pop(0)
    for move in moves:
        new_state=state^move
        if not states_viewed[new_state]:
            states_to_check.append(new_state)
            states_viewed[new_state]=True
            states_moves[new_state]=states_moves[state]+1

for _ in range(num_cases):
    board=[]
    board.append(sys.stdin.readline().strip())
    board.append(sys.stdin.readline().strip())
    board.append(sys.stdin.readline().strip())
    final_state=board2int(board)
    print states_moves[final_state]


