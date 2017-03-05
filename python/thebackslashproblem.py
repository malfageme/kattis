import sys

def escape_char(c, slash):
    if (ord(c) >= ord('!') and ord(c) <= ord('*')) or (ord(c) >= ord('[') and ord(c) <= ord(']')):
        return slash+c
    else:
        return c

while True:
    n_s = sys.stdin.readline()
    if not n_s:
        break
    n = int(n_s)

    c = 0
    for _ in range(n):
        c = 2*c+1

    slashes = '\\' * c
    text = sys.stdin.readline().strip()

    new_text = "".join([escape_char(c, slashes) for c in text])

    print new_text
