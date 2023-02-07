# 1509. 팰린드롬 분할

word = input()
N = len(word)

cnt = 0

dp = [[0]*N for _ in range(N)]

for length in range(N):
    for start in range(N-length):
        end = start + length

        # 글자수 1개
        if length == 0:
            dp[start][end] = True
            continue

        # 글자수 2개
        elif length == 1:
            if word[start] == word[end]:
                dp[start][end] = True
        
        # 양 끝이 같고 양 끝을 제외한 나머지가 팰린드롬이면 True
        else:
            if word[start] == word[end] and dp[start+1][end-1] == True:
                dp[start][end] = True

print(*dp,sep='\n')