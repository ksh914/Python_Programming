```
def solution(n, lost, reserve):
    _reserve = set(reserve)-set(lost) # 문제의 마지막 조건을 위한 set()
    _lost = set(lost)-set(reserve)
    
    for A in _reserve:
        f = A-1
        b = A+1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    
    return n - len(_lost)
```