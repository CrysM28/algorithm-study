# 11054. 가장 긴 바이토닉 부분 수열

n = int(input())
arr = list(map(int, input().split()))
arr_reverse = arr[::-1]

inc = [1]*n
dec = [1]*n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            inc[i] = max(inc[i], inc[j]+1)
        if arr_reverse[j] < arr_reverse[i]:
            dec[i] = max(dec[i], dec[j]+1)

dec = dec[::-1]
res = [0] * n
for i in range(n):
    res[i] = inc[i] + dec[i] - 1

print(max(res))