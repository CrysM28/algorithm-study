# 1966. 프린터 큐
from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    docs_imp = deque(map(int, input().split()))
    docs_idx = deque([i for i in range(N)])

    cnt = 1
    while docs_imp:
        max_imp = max(docs_imp)
        imp = docs_imp.popleft()
        idx = docs_idx.popleft()

        if imp < max_imp:
            docs_imp.append(imp)
            docs_idx.append(idx)
        else:
            if idx == M:
                break
            cnt += 1
    
    print(cnt)
