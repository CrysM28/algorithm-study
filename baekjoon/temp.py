# for easy problems

from itertools import combinations

n,m = map(int, input().split())
a = list(combinations(range(1,n+1),m))
print(a)
