# 1764. 듣보잡

n, m = map(int, input().split())
d_not = set([input() for _ in range(n)])     # 듣도 못한 사람
b_not = set([input() for _ in range(m)])     # 보도 못한 사람
db_not = []

for d in d_not:
    if d in b_not:
        db_not.append(d)

# 더 간단한 방법
## db_not = list(d_not.intersection(b_not))

db_not.sort()
print(len(db_not))
print(*db_not, sep="\n")