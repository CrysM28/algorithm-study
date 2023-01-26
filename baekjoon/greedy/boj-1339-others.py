n = int(input())

# dict 대신 idx로 관리 -> 더 빠름!
digit = [0]*26
for _ in range(n):
    num = list(input().rstrip())
    for i in range(len(num)):
        digit[ord(num[i])-65] += 10 ** (len(num)-i-1)
digit.sort(reverse=True)

ans = 0
dig = 9
for i in digit:
    if not i:
        break
    ans += i*dig
    dig -= 1
print(ans)