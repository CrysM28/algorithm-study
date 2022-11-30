# 1806. 부분합

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0

ps = [0]
for i in range(N):
    tmp = ps[i] + arr[i]
    if tmp >= S and end == 0:
        end = i+1
    ps.append(tmp)

answer = end - start

if ps[-1] < S:
    print(0)
else:
    while end <= N:
        start += 1

        tmp = ps[end] - ps[start]

        if tmp >= S:
            answer = min(answer, end-start)
        else:
            end += 1

    print(answer)