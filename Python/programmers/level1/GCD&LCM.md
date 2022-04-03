```
def solution(n,m):
    answer=[]
    Min = min(n,m)
    M_min=1
    M_max=1
    for i in range(2,Min+1):
        if n%i==0 and m%i==0:
           M_min = i
    answer.append(M_min)
    
    for j in range(n*m+1, max(n,m)-1,-1):
        if j%n==0 and j%m==0:
            M_max=j
    answer.append(M_max)
    
    return answer
```