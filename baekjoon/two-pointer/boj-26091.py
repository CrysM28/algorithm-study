# 26091. 현대모비스 소프트웨어 아카데미

N, M = map(int, input().split())
ppl = list(map(int, input().split()))
ppl.sort()

team = 0

start = 0
end = N-1
while start < end:
    if ppl[start] + ppl[end] >= M:
        team += 1
        end -= 1
    start += 1

print(team)