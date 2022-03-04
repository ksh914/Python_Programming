import sys
from collections import Counter
N=int(input())
ML=[]
for i in range(N):
    ML.append(int(sys.stdin.readline()))
    
ML.sort()
print(Counter(ML).most_common)