# 앞 2개 묶음에서 최소값 삭제하는 것을 k번 반복
## 계속 맨 앞에는 큰 값만 남게 되므로 최적해 찾을 수 있음

### failed -> 역순 예제 실패, 일부 예제 타임아웃

def solution(number, k):
    idx = 0
    local_max = number[0]

    while k != 0:
        print(k, local_max, idx, number)

        # 현 idx 값이 최대일 때
        if number[idx] >= local_max:
            local_max = number[idx]

            # 앞에 뭐가 있는데 최고값 찾았으면 앞에걸 지워야 함
            if idx != 0:
                while k > 0 and idx > 0:
                    if number[idx] > number[idx-1]:
                        k -= 1
                        idx -= 1
                        number = number.replace(number[idx], "", 1)
                    else:
                        idx -= 1
                continue

            # 최대값이 연속이면 계속 넘김
            while number[idx] == local_max:  
                idx += 1
            continue

        # 현 최고값과 뒷 값과 비교하여 작은 값을 삭제
        if number[idx] < local_max:
            if idx + 1 >= len(number):
                idx -= 1
            if number[idx] < number[idx+1]:
                number = number.replace(number[idx], "", 1)
            else:
                number = number.replace(number[idx+1], "", 1)
            k -= 1

    return number

#print(solution("21613", 4))
#print(solution("4177252841", 4))
#print(solution("8888844", 2))
#print(solution("88982199333", 4))
print(solution("87654321", 3))
