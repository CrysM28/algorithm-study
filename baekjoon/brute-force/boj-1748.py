# 1748. 수 이어 쓰기 1

N = int(input())
n_len = len(str(N))

# 이전 자릿수 전부
ans = 0
for i in range(1, n_len):
    ans += i * (10**(i-1)) * 9

# 현 자릿수 개수만큼
ans += (N - 10**(n_len-1) + 1) * n_len

print(ans)
