# 셀프 넘버

def d(num):
    result = num
    for n in str(num):
        result += int(n)
    return result

self_nums = set()
for i in range(1, 10001):
    self_nums.add(d(i))

for i in range(1, 10001):
    if i not in self_nums:
        print(i)