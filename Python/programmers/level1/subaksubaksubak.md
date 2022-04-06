```
def solution(n):
    answer = ''
    A = '수'
    B = '박'
    for i in range(n):
        if i%2==0:
            answer+='수'
        else:
            answer +='박'
    return answer
```