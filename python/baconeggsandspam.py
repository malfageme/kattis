import sys

while True:
    num_days = int(sys.stdin.readline())
    if num_days == 0:
        break
    cook_list = {}
    for _ in range(num_days):
        line = sys.stdin.readline().split()
        for food in line[1:]:
            try:
                cook_list[food].add(line[0])
            except:
                cook_list[food] = set([line[0]])

    for food in sorted(cook_list.keys()):
        print "{} {}".format(food, " ".join(sorted(cook_list[food])))

    print
