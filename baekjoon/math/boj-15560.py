# 15560. 구간 합 최대? 1

N, Q, U, V = map(int, input().split())
nums = [0] + list(map(int, input().split()))

# 누적합
ps = [0] * (N+1)
for i in range(1, N+1):
    ps[i] = ps[i-1] + nums[i]

#print(ps)

for _ in range(Q):
    C, A, B = map(int, input().split())

    # 최대값 구하기: U*수열(i~j) + V*(j-i)
    if C == 0:
        pass

    # 값 변경: 수열, 누적합 갱신
    else:
        diff = nums[A] - B
        nums[A] = B
        for i in range(A, N+1):
            ps[i] -= diff
