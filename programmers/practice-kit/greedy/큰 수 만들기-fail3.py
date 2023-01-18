
def solution(number, k):
    idx = 0
    local_max = number[0]

    while k != 0:

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

