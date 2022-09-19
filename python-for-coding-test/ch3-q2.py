# M이 클 때 시간초과 나지 않는 방법

N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

# 가장 큰 수가 더해지는 횟수
count = ((M // (K + 1)) * K) + (M % (K + 1))

result = 0
result += (count) * data[N - 1]         # 제일 큰수
result += (M - count) * data[N - 2]     # 두번째로 큰 수

print(result)
