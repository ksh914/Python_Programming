```
def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=False)
    for i in range(len(A)):
        answer +=A.pop()*B.pop()
    

    return answer
```