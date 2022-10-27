# 25632. 소수 부르기 게임

def prime_list(start, end):
    array = [True] * (end + 1)

    for i in range(2, int(end**0.5) + 1):
        if array[i] == True:
            for j in range(i + i, end + 1, i):
                array[j] = False

    return [i for i in range(start, end + 1) if array[i] == True]


A, B = map(int, input().split())
C, D = map(int, input().split())

# 각자 부를 수 있는 소수의 수
yt, yj = 0, 0

# 각자 부를 수 있는 소수 목록
yt_list = prime_list(A, B)
yj_list = prime_list(C, D)


# 1. 동시에 부를 수 있는 소수 개수
yt_set = set(yt_list)
yj_set = set(yj_list)
same_prime = len(yt_set & yj_set)

yt = (same_prime // 2) + (same_prime % 2)
yj = same_prime // 2

# 2. 각자 부를 수 있는 소수 개수
yt += len(yt_list) - same_prime
yj += len(yj_list) - same_prime


if yt > yj:
    print("yt")
else:
    print("yj")
