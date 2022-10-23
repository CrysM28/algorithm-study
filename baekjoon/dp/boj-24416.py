# 24416. 알고리즘 수업 - 피보나치 수 1
import sys
sys.setrecursionlimit(10 * 4)

n = int(input())

rec_num = 0
def fib_rec(i):
    global rec_num
    if i == 1 or i == 2:
        return 1
    rec_num += 1
    return fib_rec(i - 1) + fib_rec(i - 2)


fib_rec(n)

# dp : 항상 n-2 번
print(rec_num+1, n - 2)





# def fib_dp(n):
#     f = defaultdict(int)
#     f[1] = 1
#     f[2] = 1
#     for i in range(3, n+1):
#         f[i] = f[i-1] + f[i-2]
#     return f[n]