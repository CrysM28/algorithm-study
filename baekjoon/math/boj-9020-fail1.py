# 9020. 골드바흐의 추측

def get_prime_list(num):
    arr = [True] * (num+1)
    for i in range(2, int(num**0.5)+1):
        if arr[i]:
            for j in range(i+i, num+1, i):
                arr[j] = False
    return [i for i in range(1, num+1) if arr[i]]


for _ in range(int(input())):
    n = int(input())

    primes = get_prime_list(n)

    left, right = len(primes)//2, len(primes)//2
    print(primes, left, right)

    while True:
        prime_sum = primes[left] + primes[right]

        if prime_sum == n:
            print(primes[left], primes[right])
            break
        elif prime_sum < n:
            right += 1
        else:
            left -= 1

