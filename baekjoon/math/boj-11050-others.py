# 11050. 이항 계수 1
## 이항계수/조합의 정의를 이용한 수학풀이 
## math에 factorial 함수가 있어서 활용할 수 있음!

from math import factorial
n, k = map(int, input().split())
result = factorial(n) // (factorial(k) * factorial(n - k))
print(result)