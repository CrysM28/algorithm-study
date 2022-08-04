# 회의실 배정
## 최적해: 먼저 끝나는 회의부터 선택하여 배치하기

answer = 0  # 사용할 수 있는 회의의 최대 개수

# 입력 처리
num = int(input())
meetings = []       # 회의 시작/끝 시간 정보
for n in range(num):
    meetings += list(map(int, input().split())),

# 끝나는 시간을 기준으로, 시간 효율을 위해 pop으로 처리할 수 있게 내림차순 정렬
meetings.sort(reverse=True, key=lambda x: (x[1], x[0]))

recent_end = 0  # 가장 마지막으로 끝난 시간

# 먼저 끝나는 회의부터 차례대로 겹치지 않게 나열
for _ in range(num):
    m = meetings.pop()
    start, end = m[0], m[1]

    if recent_end <= start:    # 회의 시간 겹치지 않으면 count 증가
        recent_end = end
        answer += 1

print(answer)
