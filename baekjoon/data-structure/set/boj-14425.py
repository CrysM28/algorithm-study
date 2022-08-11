# input 처리
n, m = map(int, input().split())
s = set()
check = []
answer = 0
for _ in range(n):    s.add(input())
for _ in range(m):    check.append(input())

# in 연산은 set이 빠르다 (해쉬 구조이기 때문)
for c in check:
    if c in s:
        answer += 1

print(answer)
