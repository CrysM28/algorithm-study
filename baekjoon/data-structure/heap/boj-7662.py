# 7662. 이중 우선순위 큐
import heapq as h
import sys
from collections import defaultdict

input = sys.stdin.readline
i = 0  # 데이터 식별자 관리 -> 삭제 여부 추적

for _ in range(int(input())):  # 테스트 케이스
    h_max = []  # 우선순위 큐로 사용할 최대힙
    h_min = []  # 최소힙
    deleted = defaultdict(bool)  # 인덱스별 삭제 여부 관리

    for _ in range(int(input())):  # 연산
        ops, n = input().split()
        n = int(n)
        i += 1  # 식별자

        # 삽입 연산
        if ops == 'I':
            h.heappush(h_max, (-n, i))
            h.heappush(h_min, (n, i))

        # 삭제하는 연산
        elif ops == 'D':
            # 비어있으면 연산 스킵
            if not h_max or not h_min:
                continue

            # 최대값 제거
            if n == 1:
                while h_max:
                    cur_max = h.heappop(h_max)
                    if not deleted[cur_max[1]]:  # False: 삭제된 적 없음
                        deleted[cur_max[1]] = True
                        break
                    # 삭제된 노드였으면 보내고 다시 pop

            # 최소값 제거
            elif n == -1:
                while h_min:
                    cur_min = h.heappop(h_min)
                    if not deleted[cur_min[1]]:
                        deleted[cur_min[1]] = True
                        break

    # 결과 출력 전 삭제된 노드인지 확인
    while h_max:
        cur_max = h.heappop(h_max)
        if not deleted[cur_max[1]]:
            break
    while h_min:
        cur_min = h.heappop(h_min)
        if not deleted[cur_min[1]]:
            break

    # 최종 결과 출력
    if deleted[cur_max[1]] or deleted[cur_max[1]]:
        print("EMPTY")
    else:
        print(cur_max[0] * (-1), cur_min[0])
