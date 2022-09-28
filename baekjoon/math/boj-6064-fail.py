# 6064. 카잉 달력
## 중국인의 나머지 정리로 쉽게 풀 수 있긴 한데
## 다른 방법으로 먼저 한 번 풀어보자 -> 머리아파요 ㅠ


for _ in range(int(input())):
    # <m:n>, <x:y>
    m, n, x, y = map(int, input().split())

    arr = [i for i in range(1, n+1)]
    k = abs(m - n)



    idx = x-1
    cnt = 0
    while True:     
        try:
            print(idx, arr[idx])
            if arr[idx] == y:
                break
            idx -= k
            cnt += 1
        except:
            cnt = -1
            break

    print("count", cnt, m, x)

    if cnt == -1:
        print(-1)
    else:
        answer = (cnt * m) + x
        print(answer)

