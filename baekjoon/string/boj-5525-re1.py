# 5525. IOIOI

N = int(input())
M = int(input())
S = input()

idx = 0
cnt = 0
res = 0

while idx+2 < M:
    if S[idx:idx+3] == "IOI":
        cnt += 1
        idx += 2

        if cnt == N:
            res += 1
            cnt -= 1
    else:
        idx += 1
        cnt = 0

print(res)


'''
시간 초과: 50점 풀이

P = "I" + "OI" * N

start, end = 0, len(P)
cnt = 0

while end < M:
    print(start, end)
    if S[start] != 'I':
        start += 1
        end += 1
        continue


    cur = S[start:end]
    print(cur)
    if cur == P:
        cnt += 1
        start += len(P)-1
        end += len(P)-1
    else:
        start += 1
        end += 1

print(cnt)
'''