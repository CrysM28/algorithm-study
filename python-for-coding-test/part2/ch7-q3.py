# 떡볶이 떡 만들기

# 결정 함수
def decision(cut_len):
    cnt = 0
    for dd in arr:
        if dd > cut_len:
            cnt += dd - cut_len
    return cnt

# 개수, 길이
n, m = map(int, input().split())
# 떡볶이
arr = list(map(int, input().split()))

result = 0

# 매개변수 탐색
start, end = 0, max(arr)
while start <= end:
    length = (start + end) // 2
    num = decision(length)
    
    # 더 길게 자를 수 있겠다
    if num >= m:
        start = length + 1
        result = length
    
    # 더 짧게 잘라야겠다
    elif num < m:
        end = length - 1

    # p.s.는 종료조건 따로 없이 끝까지 찾아봄 -> for 최적해

print(result)
