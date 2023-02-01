# 7662. 이중 우선순위 큐
import heapq as h
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    min_heap = []
    max_heap = []
    i = 0
    deleted = set()

    k = int(input())
    for _ in range(k):
        ops, n = input().split()
        n = int(n)

        if ops == 'I':
            i += 1
            h.heappush(min_heap, (n,i))
            h.heappush(max_heap, (-n,i))
        else:
            if not min_heap or not max_heap:
                continue

            if n == -1:
                while min_heap:
                    val, idx = h.heappop(min_heap)
                    if idx not in deleted:
                        deleted.add(idx)
                        break
            else:
                while max_heap:
                    val, idx = h.heappop(max_heap)
                    if idx not in deleted:
                        deleted.add(idx)
                        break

    # print(min_heap)
    # print(max_heap)
    # print(deleted)

    min_val = "EMPTY"
    max_val = "EMPTY"
    while min_heap:
        val, idx = h.heappop(min_heap)
        if idx not in deleted:
            min_val = val
            break

    while max_heap:
        val, idx = h.heappop(max_heap)
        if idx not in deleted:
            max_val = -val
            break

    if min_val == "EMPTY" or max_val == "EMPTY":
        print("EMPTY")
    else:
        print(max_val, min_val)