## 시간 초과

import sys
import math

# 1로 이루어진 n의 배수 중 가장 작은 수의 자리수를 반환
def find_1(n):
    n_mult_factor = 1               # 배수 곱하는 인자 
    
    # 1로 이루어진 n의 배수 찾을 때까지 반복
    while True:
        n_mult = n * n_mult_factor      # 배수 계산
        n_digit = int(math.log10(n_mult))    # n 자릿수 계산
   
        # 모든 자릿수가 1인지 확인
        for i in range(n_digit+1):      
            curr_digit = (n_mult % (10**(i+1))) // (10**i)  # 현재 자릿수의 수 구하기
            if curr_digit != 1:      # 하나라도 1이 아니면 바로 끝내고 다음 배수로
                break
            if i == n_digit:
                return (n_digit+1)        

        n_mult_factor += 1              # 다음 배수


while True:
    # 숫자 아니면 종료
    try:
        n = int(sys.stdin.readline())
    except:
        break   

    print(find_1(n))

