## 시간 초과

import sys
import math

# 1로 이루어진 n의 배수 중 가장 작은 수의 자리수를 반환
def find_1(n):
    n_mult = 0          # n의 배수

    # 답이 안 나오면 새로운 배수로 계속
    while True:
        n_mult += n 
        i = 1           # 자릿수

        # 배수의 각 자리 검사
        while True:  
            # 현재 자릿수의 수 구하기
            n_temp = (n_mult % (10**i))
            curr_digit = n_temp // (10**(i-1))  
            
            # 하나라도 1이 아니면 바로 끝내고 다음 배수로
            if curr_digit != 1:
                break
        
            # 이 결과가 같으면 마지막 자릿수이므로 정답
            if n_temp == n_mult:
                return i

            # 위의 조건을 모두 통과했으면 다음 자릿수 검사
            i += 1


while True:
    # 숫자 아니면 종료
    try:
        n = int(sys.stdin.readline())
        print(find_1(n))
    except:
        break   


