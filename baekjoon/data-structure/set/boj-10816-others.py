# 이분탐색 없이 dict 사용한 풀이
## cardnumberA에 있는 숫자를 key, 나타난 횟수를 value로 해서 탐색

import sys

input = sys.stdin.readline
print = sys.stdout.write

dic = {}

int(input().strip())
arr = input().strip().split()
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

int(input().strip())
arr = input().strip().split()
for i in arr:
    if i in dic:
        print(str(dic[i]) + " ")
    else:
        print("0 ")