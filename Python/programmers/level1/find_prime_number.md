```
def solution(n):
    answer = 0
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            answer+=1
    return answer
```
처음에는 이런식으로 코드를 짰지만, 시간복잡도에서 시간초과가 걸려서 10번째 시도부터 풀리지 않았다.

따라서 이를 set형태로 2~n까지 설정한 뒤, 작은 수부터 n번째까지 제곱, 세제곱한 수가 set안에 있다면

지우는 식으로 전개를 하였다. 마치 동적계획법과 비슷한 문제 풀이법이었다.

```
def solution(n):
    answer = set(range(2,n+1))
    
    for i in range(2,n+1):
        if i in answer:
            answer -= set(range(i*2,n+1,i))
                
        
    return len(answer)
```