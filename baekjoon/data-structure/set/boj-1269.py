# 1269. 대칭 차집합

input()
a = set(map(int, input().split()))
b = set(map(int, input().split()))

len1 = len(a-b)
len2 = len(b-a)

print(len1+len2)