# 2581. 소수 

def is_prime(n):
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

M = int(input())
N = int(input())

prime_sum = 0
prime_min = 10001


for i in range(M, N+1):
    if i == 1:
        continue
    if is_prime(i):
        prime_sum += i
        if prime_min == 10001:
            prime_min = i

if prime_min != 10001:
    print(prime_sum)
    print(prime_min)
else:
    print(-1)
