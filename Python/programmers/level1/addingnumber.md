```
def solution(n):
    answer = 0
    ML = [int(a) for a in str(n)]
    for i in range(len(ML)):
        answer += ML[i]
    
    return answer
```