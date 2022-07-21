    while True:
        if scv[0] < K:
            low1 = scv.popleft()
            low2 = scv.popleft()
            new_scv = low1 + low2 * 2
            scv.append(new_scv)
            mix += 1
        else:
            break


from collections import deque
import heapq

def solution(scv, K):
    mix = 0
    heapq.heapify(scv)
    
    while True:
        scv = max_heap(scv)
        print(scv)
        
        # 힙 트리 높이 구하기
        temp = len(scv)        
        while temp % 2 != 0:
            height += 1
            temp = temp // 2

        # 힙의 마지막 노드만 훑음
        for i in range(pow(2,height-1), len(scv)):
            min_vals.append(scv[i])
        print(min_vals)
        min1 = min(min_vals)
        scv.remove(min(min_vals))
        min_vals.remove(min(min_vals))
        min2 = min(min_vals)
        scv.remove(min(min_vals))
        min_vals.remove(min(min_vals))

        print(min1, min2)
        
        new_val = min1 + min2 * 2
        scv.append(new_val)
        
        print(scv)        
        scv = max_heap(scv)        
        print(scv)

        
        break

    return mix





