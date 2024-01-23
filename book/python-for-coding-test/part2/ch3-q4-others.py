# 1이 될 때까지
## 최적화 -> 일일이 1을 빼지 않고 배수가 되게끔 한 번에 빼기

n, k = map(int, input().split())

count = 0
while n >= k:
    target = (n//k) * k     # 배수
    count += n - target     # 배수 만들기 위해 1 빼야하는 횟수
    n = target

    n //= k
    count += 1

count += n-1    # 1 될때까지

print(count)