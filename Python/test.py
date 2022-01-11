N = int(input())
for _ in range(N):
    nums, s = input().split()
    text=""
    for i in s:
        text+=i * int(nums)
    print(text)