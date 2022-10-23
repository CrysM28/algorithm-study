# 16953. A -> B
a, b = map(int, input().split())

q = [a]
next_q = []
min_ops = 0
found = False

while q:
    val = q.pop()

    if val == b:
        found = True
        break
    
    next_val1 = val * 2
    if next_val1 <= b:
        next_q.append(next_val1)
    next_val2 = val*10 + 1
    if next_val2 <= b:
        next_q.append(next_val2)

    if not q:
        q = next_q[:]
        next_q.clear()
        min_ops += 1


if found:
    print(min_ops + 1)
else:
    print(-1)
