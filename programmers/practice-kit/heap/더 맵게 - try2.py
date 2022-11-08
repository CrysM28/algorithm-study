import heapq as h

def solution(scoville, K):
    h.heapify(scoville)
    
    answer = 0
    
    while len(scoville) > 1:
        scov1 = h.heappop(scoville)
        scov2 = h.heappop(scoville)
        
        if scov1 >= K:
            h.heappush(scoville, scov1)
            break

        new_scov = scov1 + (scov2 * 2)
        h.heappush(scoville, new_scov)
        answer += 1

    tmp = h.heappop(scoville)
    if tmp < K:
        answer = -1
        
    return answer