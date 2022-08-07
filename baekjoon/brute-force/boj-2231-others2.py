# 다른 풀이 2
## others1이랑 같은데 한 줄 때문에 시간이 1540 -> 72 ms로 줄었음..

n = input()
l = len(n)
n = int(n)

###########
start = max(0, n - 9 * l)  # 이게 뭐하는 거길래? ..
###########

for i in range(start, n + 1):
    if n == i + sum(map(int, str(i))):
        print(i)
        break
    if i == n:
        print(0)
