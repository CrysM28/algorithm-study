# 3:30? ~ 3:40

# 진법 변환
import string
tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

# 소수 판별
def is_prime(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True 



def solution(n, k):
    # 진법 변환
    n = convert(n,k)

    # 0 기준으로 문자열 나누기
    candidates = []
    tmp = ''
    for w in n:
        if w == '0':
            if tmp:
                candidates.append(int(tmp))
            tmp = ''
        else:
            tmp += w
    if tmp:
        candidates.append(int(tmp))

    print(candidates)

    # 소수 세기
    answer = 0
    for c in candidates:
        if is_prime(c):
            answer += 1

    return answer



print(solution(110011,10))