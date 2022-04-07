```
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for p,c in zip(participant,completion):
        if p !=c:
            return p
    
    return participant.pop()
```

해시 문제라는데 해시가 뭔지 몰라서 공부를 더 할 필요가 있다.