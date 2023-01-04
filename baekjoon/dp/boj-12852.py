# 12852. 1로 만들기 2
from collections import defaultdict

n = int(input())

# 횟수, 이전번호
ops = defaultdict(int)
prev = defaultdict(int)

for i in range(2, n+1):
    ops[i] = ops[i-1] + 1
    prev[i] = i-1

    if i % 3 == 0 and ops[i] > ops[i//3] + 1:
        ops[i] = ops[i//3] + 1
        prev[i] = i//3
    
    if i % 2 == 0 and ops[i] > ops[i//2] + 1:
        ops[i] = ops[i//2] + 1
        prev[i] = i//2


print(ops[n])

prev_num = n
print(prev_num, end=" ")
while prev_num != 1:
    prev_num = prev[prev_num]
    print(prev_num, end=" ")