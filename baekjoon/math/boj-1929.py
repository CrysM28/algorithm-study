# 1929. 소수 구하기


# 에라토스테네스의 체 이용한 소수 판별 함수
def primes(start, end):
    arr = [False, False] + [True] * (end)   # 0, 1은 소수가 아님
    for i in range(2, int(end**0.5) + 1):
        if arr[i]:  # i가 소수인 경우
            for j in range(i+i, end+1, i):    # i의 배수 제거
                arr[j] = False
    return [i for i in range(start, end+1) if arr[i]]


m,n = map(int, input().split())
print(*primes(m,n), sep="\n")
