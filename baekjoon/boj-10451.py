# 10451. 순열 사이클
## 생각나는 반례가 없네
## 왜 parent 개수 세는건 안되는걸까?
## 일단 cycle 만들어질때마다 +1 하는 방식으로는 됐음
## DFS 풀이로도 풀어보는게 좋을듯

from collections import defaultdict, Counter

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return True
    elif a > b:
        parent[a] = b
    else:
        parent[b] = a
    return False



T = int(input())
for _ in range(T):
    
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    parent = [i for i in range(N+1)]
    # graph = defaultdict(list)
    # for i, a in enumerate(arr):
    #     graph[i+1].append(a)
    

    print(parent)

    ans = 0
    for i in range(1, N+1):
        if union(i, arr[i]):
            ans += 1
    
    print(parent)
    #print(parent)
    #c = Counter(parent)
    #print(len(c)-1)
    print(len(set(parent))-1)
    print(ans)