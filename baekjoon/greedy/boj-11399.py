# 11399. ATM
## 앞 사람 시간이 적을수록 덜 걸리므로 정렬해서 계산

n = int(input())  # 사람 수
times = sorted(list(map(int, input().split())))  # 인출 시간 -> 정렬
t = 0   # 총 걸린 시간

for i, p in enumerate(times):
    t += p * (n-i)

print(t)

