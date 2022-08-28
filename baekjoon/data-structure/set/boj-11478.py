# 11478. 서로 다른 부분 문자열의 개수

s = input()
ps = set()

for i in range(1, len(s) + 1):
    for j in range(len(s)):
        ps.add(s[j:j+i])

print(len(ps))