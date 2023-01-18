# 10246. 부동산 경매
import sys
input = sys.stdin.readline

while True:
    money = int(input())

    if money == 0:
        break
    elif money < 2:
        print(0)
        continue

    # 집 하나 (딱 money원)
    ans = 1

    # 더해서 만들 수 있는 집
    for i in range((money+1)//2, 1, -1):
        tmp = 0
        idx = i

        while True:
            tmp += idx
            idx -= 1

            if tmp == money:
                print(i, idx)
                ans += 1
                break
            elif tmp > money:
                break
            
            if idx < 2:
                break


    print(ans)
