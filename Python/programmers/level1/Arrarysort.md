```
def solution(n):
    answer = 0
    N = list(str(int(n)))
    N.sort(reverse=True)
    answer = int("".join(N))
        
    return answer

s=solution(118372)
print(s)
```