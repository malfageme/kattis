import sys
from operator import itemgetter

adrian="ABC"
bruno="BABC"
goran="CCAABB"

num_questions=int(sys.stdin.readline())
answers=sys.stdin.readline().strip()

adrian_check=[]
bruno_check=[]
goran_check=[]
for i in range(num_questions):
    adrian_check.append(answers[i]==adrian[i%len(adrian)])
    bruno_check.append(answers[i]==bruno[i%len(bruno)])
    goran_check.append(answers[i]==goran[i%len(goran)])

results={
            "Adrian":adrian_check.count(True),
            "Bruno":bruno_check.count(True),
            "Goran":goran_check.count(True)
        }

max_answered=max(results.values())
print max_answered
for name in sorted([x[0] for x in results.items() if x[1]==max_answered]):
    print name

