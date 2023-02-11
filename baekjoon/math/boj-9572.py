# 9572. 1의 개수 세기

def check(n):
    cnt = 0
    bin_num = bin(n)[2:]    # 0b 떼기
    l = len(bin_num)

    for i in range(l):
        if bin_num[i] == '1':
            pow = l-i-1
            n -= 2**pow

            # 맨 앞 제외 1 개수 (dp)
            cnt += ps[pow]
            # 맨 앞 1 개수
            cnt += n + 1

    return cnt


A, B = map(int, input().split())

# 누적합
ps = [0] * (60)
for i in range(1, 60):
    ps[i] = 2**(i-1) + 2*ps[i-1]

ans = check(B) - check(A-1)
print(ans)