# 25630. 팰린드롬 소떡소떡
n = int(input())
stst = list(input())

left, right = 0, n-1
magic = 0

while left <= right:
    if stst[left] != stst[right]:
        magic += 1
    left += 1
    right -= 1

print(magic)
