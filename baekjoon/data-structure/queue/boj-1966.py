# 1966. 프린터 큐
## 프로그래머스 "프린터"와 동일한 문제 -> 다시 풀어보는 마음으로.
from collections import deque

for _ in range(int(input())):
    # input
    n, m = map(int, input().split())
    imp = deque(input().split())
    idx = deque([x for x in range(n)])      # 인덱스 관리를 위한 배열
    order = []                              # 프린트 순서 저장

    for _ in range(n):
        while imp[0] != max(imp):       
            imp.append(imp.popleft())   # 가장 중요한 문서가 아니면 뒤로
            idx.append(idx.popleft())   # 인덱스 배열도 같이 관리
        imp.popleft()                   # 프린트 했으므로 큐에서 삭제
        order.append(idx.popleft())     # 프린트 한 것의 원래 인덱스를 저장 (순서대로)

    print(order.index(m)+1)