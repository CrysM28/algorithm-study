# 두 배열의 원소 교체

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

# b에서 가장 큰 k개의 합 + a에서 가장 작은 k개를 제외한 합
ans = sum(b[-k:n]) + sum(a[-(n-k):n])
print(ans)