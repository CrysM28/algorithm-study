# 7662. 이중 우선순위 큐
## 시간초과 - 코드 깔끔하긴 한데 여전히 시간초과...
import heapq as h
import sys

input = sys.stdin.readline

for _ in range(int(input())):       # 테스트 케이스
    myheap = []  # 우선순위 큐로 사용할 (최소)힙

    for _ in range(int(input())):   # 연산
        ops, n = input().split()
        n = int(n)
        
        # 삽입 연산
        if ops == 'I':
            h.heappush(myheap, n)
        
        # 삭제 연산
        elif ops == 'D':
            # 비어있으면 연산 스킵
            if not myheap:
                continue

            # 최대값 제거
            if n == 1:
                myheap = h.nlargest(len(myheap), myheap)[1:]
                h.heapify(myheap)

            # 최소값 제거
            elif n == -1:
                cur_min = h.heappop(myheap)

    # 결과 출력
    if not myheap:
        print("EMPTY")
    else:
        print(*h.nlargest(1, myheap), h.heappop(myheap))