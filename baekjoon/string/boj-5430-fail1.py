# 5430. AC
## 시간 초과

from collections import deque

for _ in range(int(input())):  # Testcase 개수
    fn = input()  # 수행할 함수 (R/D)
    n = int(input())  # 배열 길이
    #arr = deque(eval(input())) # 배열
    arr = eval(input()) # 배열


    # 직접 뒤집지 말고, 포인터를 왼쪽/오른쪽 끝으로 놓는 것으로
    reverse = False
    idx = 0

    for p in fn:
        if p == "R":
            #arr.reverse() -> 함수 사용 시 시간초과
            if reverse:
                reverse = False
                idx = 0
            else:
                reverse = True
                idx = len(arr) - 1
        elif p == "D":
            if len(arr) == 0:
                arr = "error"
                break
            else:
                if reverse:
                    arr = arr[:idx]
                    idx -= 1
                else:
                    arr = arr[1:]
                    
    if arr != "error":  # error 아니면 list로 출력
        arr = list(arr)
        if reverse:  # reverse 상태면 뒤집어서 출력
            arr = arr[::-1]

        # 출력 형식
        ans = "["
        for a in arr:
            ans += str(a) + ","
        ans = ans[:len(ans)-1]
        ans += "]"
        print(ans)

    else:
        print(arr)  # error