# 18110. solved.ac
## 파이썬의 round는 오사오입 (0.5 초과일 때 올림하는 방식)
## 따라서 일반적인 반올림을 위해선 직접 구현할 필요가 있음

n = int(input())
cut = n * 0.15
if cut >= int(cut)+0.5:
    cut = int(cut)+1
else:
    cut = int(cut)

#print(cut)

# 난이도
diff = []
for _ in range(n):
    diff.append(int(input()))

diff.sort()
diff = diff[cut:n-cut]

print(diff)

div = n - cut*2
if div == 0:
    div = 1

ans = sum(diff) / div
if ans >= int(ans)+0.5:
    ans = int(ans)+1
else:
    ans = int(ans)

print(ans)
