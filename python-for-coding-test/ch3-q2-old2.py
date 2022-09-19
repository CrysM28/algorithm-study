# 큰 수의 법칙
## 효율 좋게 바꿔보기 -> 하지만 반복문 때문에 O(n) 이므로 n이 크면 시간초과됨

import time
start_time = time.time() # 측정 시작

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
answer = 0

for i in range(m):
    if ((i+1) % k) == 0:
        answer += a[-2]
    else:
        answer += a[-1]

print(answer)

end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력