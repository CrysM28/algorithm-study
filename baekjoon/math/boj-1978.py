# 1978. 소수 찾기

def prime_list(n):
    arr = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if arr[i] == True:
            for j in range(i + i, n+1, i):  
                arr[j] = False
    return [i for i in range(2, n + 1) if arr[i] == True]


int(input())
numbers = list(map(int, input().split()))
primes = prime_list(max(numbers))
count = 0

for n in numbers:
    if n in primes:
        count += 1

print(count)
