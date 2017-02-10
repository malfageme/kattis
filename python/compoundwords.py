import sys

words=[]

for line in sys.stdin:
    words+=line.split()

new_words=set([])
for word in words:
    for suffix in words:
        if suffix!=word:
            new_words.add(word+suffix)
            new_words.add(suffix+word)

for word in sorted(new_words):
    print word
