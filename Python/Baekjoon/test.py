import sys
MN=0
N,K = map(int, sys.stdin.readline().split())
ML = []
for i in range(N):
    ML.append(int(sys.stdin.readline()))
    
for j in range(-1,-(N+1),-1):
    if K==0:
        break
    if K>ML[j]:
        MN +=K//ML[j]
        K %=ML[j]
        
print(MN)
        
