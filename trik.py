import sys

conversion_table="ABC"
moves=sys.stdin.readline().strip()

def doMove(state, move):
    offset=((1,0,2),(0,2,1),(2,1,0))
    new_state=[state[offset[move][x]] for x in range(len(state))]
    return new_state

state=[1,0,0]
for move in moves:
    state=doMove(state, conversion_table.find(move))

print state.index(1)+1
