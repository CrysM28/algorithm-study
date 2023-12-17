
is_self = [False] * 10001

for i in range(1, 10001):
    str_i = str(i)
    n = len(str_i)
    next_num = i
    for x in range(n):
        next_num += int(str_i[x])
    
    if next_num < 10001:
        is_self[next_num] = True


for i in range(1, 10001):
    if not is_self[i]:
        print(i)
    


