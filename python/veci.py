import sys
from itertools import permutations


x=sys.stdin.readline().strip()
x_int=int(x)

min_guess=None
for guess in permutations(x):
    guess_int=int("".join(guess))
    if guess_int>x_int:
        if not min_guess or guess_int<min_guess:
            min_guess=guess_int
          

print min_guess if min_guess else 0
