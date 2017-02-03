import sys

name=sys.stdin.readline().strip()

new_name=""

for c in name:
    if c!=new_name[-1:]:
        new_name+=c

print new_name
