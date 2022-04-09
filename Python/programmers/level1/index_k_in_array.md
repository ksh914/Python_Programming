```
def solution(array, commands):
    answer = []
    for N in range(len(commands)):
        i,j,k = commands[N][0],commands[N][1],commands[N][2]
        ML = array[i-1:j]
        ML.sort()
        answer.append(ML[k-1])
    return answer
```

```

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
```