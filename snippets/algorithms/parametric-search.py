# 최대값 (upper bound) 매개변수 탐색
## 가정: 잘린 길이가 적어도 m이 되도록 자를 수 있는 최대값 구하기

# 결정 함수
def decision(x):
    pass


# 개수, 길이
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# end: 답으로 가능한 최대값
start, end = 0, max(arr)
answer = 0

# 매개변수 탐색
while start <= end:
    mid = (start + end) // 2

    # 결정 함수 결과
    result = decision(mid)
    
    # 일단 이 상태면 조건은 만족하니 저장해두는데, 더 길게 잘라도 되겠다
    if result >= m:
        answer = mid
        start = mid + 1
        
    # 더 짧게 잘라야겠다
    elif result < m:
        end = mid - 1

    # 최적해를 찾기 위해 종료조건 따로 없이 끝까지 탐색


print(answer)
# print(end)
