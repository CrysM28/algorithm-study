# 20529. 가장 가까운 세 사람의 심리적 거리

from collections import defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    ans = int(1e9)
    n = int(input())
    mbti = list(input().split())
    
    ## 같은 mbti 3개 이상이면 거리가 무조건 0 -> 비둘기집 원리
    ### 이런 예외조건을 잘 찾으면 brute-force 시간을 줄일 수 있음!
    if n > 32:
        ans = 0
    else:
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    # print(mbti[i], mbti[j], mbti[k])
                    cnt = 0

                    for x in range(4):
                        if mbti[i][x] != mbti[j][x]:
                            cnt += 1
                        if mbti[i][x] != mbti[k][x]:
                            cnt += 1
                        if mbti[j][x] != mbti[k][x]:
                            cnt += 1
                    
                    # print("cnt", cnt)
                    ans = min(ans, cnt)


    print(ans)
