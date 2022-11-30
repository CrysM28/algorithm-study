n, m = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
total = 0
h = 0

for i in arr:
    total += i
    if total < m: continue
    while total > m:
        total -= arr[h]
        h += 1
    if total == m: count += 1

print(count)