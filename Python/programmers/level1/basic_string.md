```
def solution(s):
    if len(s)==4 or len(s)==6:
        for i in range(len(s)):
            if not s[i].isdigit():
                return False
        return True
    else:
           
        return False
```

이번 문제에서 주목해야 할 점은 isdigit() 이다.

isdigit()은 문자를 검사해서 digit(숫자)인지 검사해주는 메소드이다. 따라서 숫자가 아니라면 False를 반환한다.