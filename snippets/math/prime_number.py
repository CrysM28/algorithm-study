# 일반적인 방법
## 시간복잡도 O(n^{1/2})

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(x**0.5) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


# 에라토스테네스의 체
## 시간복잡도 O(nloglogn)

def prime_list(n):
    # 초기화: 모든 수를 소수(True)로 간주
    array = [True] * (n + 1)

    # 2부터 n의 제곱근까지의 모든 수를 확인
    for i in range(2, int(n**0.5) + 1):
        if array[i] == True:  # i가 소수인 경우
            for j in range(i + i, n + 1, i):  # i 제외 i의 배수를 False 설정
                array[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n + 1) if array[i] == True]
