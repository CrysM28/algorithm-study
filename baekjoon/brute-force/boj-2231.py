# 2231. 분해합

n = input()

def get_ctor():
    # 입력인 자릿수 수까지 0부터 일일이 돌리기
    for i in range(10**len(n)):      
        # i의 분해합 구하기
        sum_i = i
        for j in range(len(str(i))):
            sum_i += int(str(i)[j])

        # i의 분해합 == n 이면 i는 n의 생성자
        if sum_i == int(n):
            return i

    # 생성자를 못 찾으면 0 출력
    return 0


print(get_ctor())
