# 13335. 트럭
from collections import deque
n, w, L = map(int, input().split())
trucks = list(map(int,input().split()))
bridge = deque([])

time = 0
weight = 0
idx = 0 

while idx < n:
    t = trucks[idx]

    while len(bridge) > w-1:
        gone = bridge.popleft()
        weight -= gone
    
    if weight + t > L:
        bridge.append(0)
    else:
        bridge.append(t)
        weight += t
        idx += 1

    time += 1

    print("===")
    print("time", time)
    print(bridge)
    print("weight", weight)


print(time+w)