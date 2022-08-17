# 5430. AC
from collections import deque

for _ in range(int(input())):  # Testcase 개수
    fn = input()  # 수행할 함수 (R/D)
    n = int(input())  # 배열 길이
    arr = deque(eval(input()))  # 배열

    reverse = False

    for p in fn:
        if p == "R":  # 시간 초과 나므로 매번 뒤집지 말기
            if reverse: reverse = False
            else: reverse = True
        elif p == "D":
            try:
                if reverse: arr.pop()
                else: arr.popleft()
            except:
                arr = "error"
                break

    if arr != "error":
        arr = list(arr)
        if reverse:  # reverse 상태면 뒤집어서 출력
            arr = arr[::-1]

        # 출력 형식
        ans = "["
        for a in arr:
            ans += str(a) + ","
        if ans != "[": ans = ans[:len(ans) - 1]
        ans += "]"
        print(ans)

    else:
        print(arr)  # error