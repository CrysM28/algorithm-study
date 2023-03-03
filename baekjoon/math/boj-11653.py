# 11653. 소인수분해

def get_prime_list(n):
    arr = [True] * (n+1)

    for i in range(2, int(n**0.5)+1):
        if arr:
            for j in range(i+i, n+1, i):
                arr[i] = False

    return [i for i in range(2, n+1) if arr]


N = int(input())
primes = get_prime_list(N)

i = 0
while N > 1:
    p = primes[i]
    if N % p == 0:
        print(p)
        N //= p
    else:
        i += 1