# 2581. 소수 
## 에라토스테네스의 체 사용한다면
## 140 -> 124 ms로 조금 더 줄일 수 있음

def prime_list(start, end):
    arr = [False, False] + [True] * (end)
    for i in range(2, int(end**(1/2)) + 1):
        if arr[i]:
            for j in range(i+i, end+1, i):
                arr[j] = False
    return [i for i in range(start, end+1) if arr[i]]

M = int(input())
N = int(input())

ans = prime_list(M, N)

if ans:
    print(sum(ans))
    print(ans[0])
else:
    print(-1)