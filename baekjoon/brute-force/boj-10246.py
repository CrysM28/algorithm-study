# 10246. 부동산 경매
import sys
input = sys.stdin.readline

while True:
    money = int(input())
    cnt = 0
    
    if money == 0:
        break
    
    elif money > 1:
        tmp = 0
        for n in range(1, int(1e9)):
            tmp += n
            if tmp >= money:
                break
            if (money-tmp)%n == 0:
                cnt += 1


    print(cnt)
