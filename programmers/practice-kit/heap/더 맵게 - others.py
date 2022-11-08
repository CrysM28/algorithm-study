
# heapq 사용
import heapq as hq
def solution(scoville, K):
    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        # len 체크문을 안에 넣어도 됨
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer


# index 활용
from heapq import heapify, heappush, heappop
def solution(scoville, K):
    heapify(scoville)
    for i in range(1000000):
        try:
            heappush(scoville, heappop(scoville)+(heappop(scoville)*2))
            if scoville[0] >= K: return i+1
        except:
            return -1