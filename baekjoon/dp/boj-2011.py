# 2011. 암호코드
MOD = int(1e6)

num = input()
num_len = len(num)

if num[0] == '0':
    print(0)

elif num_len < 2:
    if int(num) == 0:
        print(0)
    else:
        print(1)
else:
    dp = [0] * (num_len+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, num_len+1):
        num1 = int(num[i-1])
        num2 = int(num[i-2])
        cur_num = num1 + num2*10

        if num1 > 0:
            dp[i] += dp[i-1] % MOD
        
        if num2 > 0 and 1 <= cur_num <= 26:
            dp[i] += dp[i-2] % MOD

    print(dp)
    print(dp[-1] % MOD)
