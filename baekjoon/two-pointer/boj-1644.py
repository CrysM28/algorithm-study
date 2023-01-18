# 1644. 소수의 연속합

def prime_list(n):
    arr = [True] * (n+1)

    for i in range(2, int(n**0.5)+1):
        if arr[i] == True:
            for j in range(i+i, n+1, i):
                arr[j] = False
    
    return [i for i in range(2, n+1) if arr[i] == True]


N = int(input())
primes = prime_list(N)

if not primes:
    print(0)
    exit(0)

left, right = 0, 0
s = primes[0]
cnt = 0

while right < len(primes):
    #print(left, right, s)
    if s < N:
        right += 1
        if right == len(primes):
            break
        s += primes[right]
    elif s > N:
        s -= primes[left]
        left += 1
    else:
        cnt += 1
        right += 1
        if right == len(primes):
            break
        s += primes[right]

print(cnt)