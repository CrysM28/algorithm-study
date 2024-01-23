# 숫자 카드 게임

n, m = map(int, input().split())

result = 0

for _ in range(n):
    arr = list(map(int, input().split()))
    min_val = min(arr)
    result = max(result, min_val)

print(result)
    
