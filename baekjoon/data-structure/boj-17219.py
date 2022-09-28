# 17219. 비밀번호 찾기
import sys
input = sys.stdin.readline
print = sys.stdout.write

# 저장, 찾으려는
n,m = map(int, input().split())

sites = dict()
for _ in range(n):
    site, pw = input().split()
    sites[site] = pw


for _ in range(m):
    site = input().rstrip()
    print(sites[site])
    print("\n")


