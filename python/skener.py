import sys

r,c,zr,zc=map(int,sys.stdin.readline().split())

new_article=[]
for line in sys.stdin:
    new_article.extend(["".join([x*zc for x in line.strip()])]*zr)

print "\n".join(new_article)
