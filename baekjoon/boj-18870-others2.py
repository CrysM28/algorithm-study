# 이렇게까지 숏코딩이 된다고?

import sys
stdin = sys.stdin.buffer
stdin.readline()
arr = list(map(int, stdin.read().split()))

dic = {x: i for i, x in enumerate(sorted(set(arr)))}

print(' '.join(map(str, [dic[x] for x in arr])))
