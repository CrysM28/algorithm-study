# 15565. 귀여운 라이언

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

RYAN = 1
APEACH = 2

res = int(1e9)
cnt = 0     # RYAN 개수

left = 0
right = 0
if dolls[right] == 1: cnt +=1


while right < N:

    if cnt == K:
        res = min(res, right - left + 1)
        if dolls[left] == RYAN: 
            cnt -= 1
        left += 1
    
    else:
        right += 1
        if right < N and dolls[right] == RYAN: 
            cnt += 1

if res < int(1e9):
    print(res)
else:
    print(-1)