```
def solution(phone_number):
    answer = ''
    ML = len(phone_number)
    for i in range(ML-4):
        answer+='*'
        
    for j in range(ML-4,ML):
        answer+=phone_number[j]
    return answer
```