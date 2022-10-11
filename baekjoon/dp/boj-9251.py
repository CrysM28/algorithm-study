# 9251. LCS

str1 = input()
str2 = input()
str1_len = len(str1) + 1
str2_len = len(str2) + 1

dp = [[0] * str2_len for _ in range(str1_len)]

for i in range(1, str1_len):
    for j in range(1, str2_len):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

#print(*dp, sep='\n')
print(dp[-1][-1])