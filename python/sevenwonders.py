import sys

cards={}

game=sys.stdin.readline().strip()

cards["T"]=game.count("T")
cards["C"]=game.count("C")
cards["G"]=game.count("G")

print sum([x**2 for x in cards.values()]) + (7*min(cards.values()))
