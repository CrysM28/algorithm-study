# 2108. 통계학
from collections import Counter

n = int(input())
nums = [int(input()) for _ in range(n)]

# 1. 산술평균
print(int(round(sum(nums) / n)))

# 2. 중앙값
print(sorted(nums)[n // 2])

# 3. 최빈값
x = Counter(nums).most_common()
x.sort(key = lambda x: x[0])
x.sort(key = lambda x: x[1], reverse = True)

if len(x) > 1 and x[0][1] == x[1][1]:   # 여러개 있으면
    print(x[1][0])                      # 두번째로 작은 수
else:
    print(x[0][0])

# 4. 범위
print(max(nums) - min(nums))
