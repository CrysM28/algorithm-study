# 1003. 피보나치 함수
import collections

t_input = int(input())
testcases = [int(input()) for _ in range(t_input)]

# fib(n)에 대해 각각 fib(0), fib(1)이 호출되는 횟수를 저장
dp_0 = collections.defaultdict(int)
dp_1 = collections.defaultdict(int)

# bottom-up (tabulation)
for n in testcases:
    dp_0[0], dp_0[1] = 1, 0
    dp_1[0], dp_1[1] = 0, 1

    for i in range(2, n + 1):
        dp_0[i] = dp_0[i - 1] + dp_0[i - 2]
        dp_1[i] = dp_1[i - 1] + dp_1[i - 2]
            
    print(dp_0[n], dp_1[n])