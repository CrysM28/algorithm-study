import heapq

def solution(scv, K):
    mix = 0
    heapq.heapify(scv)
    
    while len(scv) >= 2:
        min1 = heapq.heappop(scv)
        min2 = heapq.heappop(scv)
        
        if min1 >= K:
            return mix
        
        new_scv = min1 + min2 * 2
        heapq.heappush(scv, new_scv)
        mix += 1
    
    if heapq.heappop(scv) >= K:
        return mix
    
    # 위 조건 모두 만족 못하면 답 X
    return -1

