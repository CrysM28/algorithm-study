# 7662. 이중 우선순위 큐
## 시간초과
import heapq as h
import sys

input = sys.stdin.readline

for _ in range(int(input())):       # 테스트 케이스
    # 우선순위 큐로 사용할 힙
    h_max = []  # 최대힙 
    h_min = []  # 최소힙
    

    for _ in range(int(input())):   # 연산
        ops, n = input().split()
        n = int(n)
        
        # 삽입 연산
        if ops == 'I':
            h.heappush(h_max,-n)
            h.heappush(h_min,n)
        
        # 삭제하는 연산
        elif ops == 'D':
            # 비어있으면 연산 스킵
            if not h_max:
                continue

            # 최대값 제거
            if n == 1:
                cur_max = h.heappop(h_max) * (-1)
                #h_min.remove(cur_max)      # O(N)

                tmp_list = []
                while h_min:
                    tmp = h_min.pop()
                    if tmp == cur_max:
                        h_min += tmp_list
                        break
                    tmp_list.append(tmp)

            # 최소값 제거
            elif n == -1:
                cur_min = h.heappop(h_min)
                #h_max.remove(cur_min * (-1))

                tmp_list = []
                while h_max:
                    tmp = h_max.pop()
                    if tmp == cur_min * (-1):
                        h_max += tmp_list
                        break
                    tmp_list.append(tmp)

    # 연산 끝난 후
    if not h_max:
        print("EMPTY")
    else:
        cur_max = h.heappop(h_max) * (-1)
        cur_min = h.heappop(h_min)
        print(cur_max, cur_min)