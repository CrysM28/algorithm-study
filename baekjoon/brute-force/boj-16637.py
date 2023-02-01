# 16637. 괄호 추가하기

def calc(a, b, ops):
    a, b = int(a), int(b)
    if ops == '+':
        return a+b
    elif ops == '-':
        return a-b
    elif ops == '*':
        return a*b


INF = int(1e9)
n = int(input())
eq = input()

# 최대값 저장
dp = [-INF] * (n//2+1)
dp[0] = int(eq[0])
if n > 2:
    dp[1] = calc(eq[0], eq[2], eq[1])

# 최소값 저장 -> 음수끼리 곱해서 최대값 되는 경우 고려
mdp = [INF] * (n//2+1)
mdp[0] = int(eq[0])
if n > 2:
    mdp[1] = calc(eq[0], eq[2], eq[1])


for i in range(4, n, 2):
    ## (연산자 제외 점화식)
    # 1. dp[i-1] + a[i]
    res1 = calc(dp[i//2 - 1], eq[i], eq[i-1])

    # 2. dp[i-2] + (a[i-1] + a[i])
    res2 = calc(eq[i-2], eq[i], eq[i-1])
    res2 = calc(dp[i//2 - 2], res2, eq[i-3])

    # 1,2 연산을 최소값과도 한 번 (음수끼리 곱 되는 경우 고려)
    res3 = calc(mdp[i//2 - 1], eq[i], eq[i-1])
    res4 = calc(eq[i-2], eq[i], eq[i-1])
    res4 = calc(mdp[i//2 - 2], res4, eq[i-3])

    dp[i//2] = max(res1, res2, res3, res4)
    mdp[i//2] = min(res1, res2, res3, res4)



# print(dp)
# print(mdp)
print(dp[-1])