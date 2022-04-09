```
def solution(arr):
    answer = []
    answer.append(arr[0])
    N=0
    for i in range(1,len(arr)):
        if answer[N]==arr[i]:
            continue
        elif answer[N]!=arr[i]:
            answer.append(arr[i])
            N+=1
    
    return answer
```

```
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
```