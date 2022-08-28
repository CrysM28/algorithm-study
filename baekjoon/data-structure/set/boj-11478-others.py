import sys
s = sys.stdin.readline().strip()
ans = set()

for i in range(len(s)):
    for j in range(i,len(s)):
        tmp = s[i:j+1]       # 이게 더 정석 풀이
        ans.add(tmp)
print(len(ans))