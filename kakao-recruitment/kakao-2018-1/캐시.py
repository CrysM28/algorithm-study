# 5분 문제훑기
# 20분만에 풀었는데 테스트케이스 몇 개 통과 못함 -> 10분 더 써서 오류해결

from collections import deque

def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize) # 자동으로 크기 조절
    time = 0

    for c in cities:
        c = c.lower()

        # cache hit
        if c in cache:
            time += 1
            cache.remove(c)
            cache.append(c)

        # cache miss
        else:
            time += 5
            cache.append(c)

    return time



#print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(4, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

#print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	))
