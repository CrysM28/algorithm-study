# 1676. 팩토리얼 0의 개수
## 임의 정밀도 / 큰 수 연산

import math

n = int(input())
fact = math.factorial(n)
fact = str(fact)[::-1]  # 뒤에서부터 체크
cnt = 0

for f in fact:
    if f == "0":
        cnt += 1
    else:
        break

print(cnt)