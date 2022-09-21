# 1439. 뒤집기

s = input()

# 0, 1의 그룹 개수
g0 = 0
g1 = 0

# 현재 수
num = s[0]

if num == '0':
    g0 += 1
else:
    g1 += 1

# 다른 숫자 그룹 개수 찾기
for ss in s:
    if num != ss: 
        num = ss
        if num == '0':
            g0 += 1
        else:
            g1 += 1

print(min(g0, g1))