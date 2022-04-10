```
def solution(a, b):
    if a<=b:
        return sum([x for x in range(a,b+1)])
    if a>=b:
        return sum([x for x in range(b,a+1)])
```

```
def solution(a,b):
    if a>b: a,b = b,a

    return sum(range(a,b+1))
```