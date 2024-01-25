# 21921. 블로그


N, X = map(int, input().split())
visit = list(map(int, input().split()))

most_visit = 0
most_day = 1

start = 0
end = X

# 누적합
ps = [0] * (N+1)
for i in range(1, N+1):
    ps[i] = ps[i-1] + visit[i-1]

while end <= N:
    cnt = ps[end] - ps[start]

    if (most_visit < cnt):
        most_visit = cnt
        most_day = 1
    elif (most_visit == cnt):
        most_day += 1

    start += 1
    end += 1


if most_visit == 0:
    print("SAD")
else:
    print(most_visit)
    print(most_day)



'''
난이도: 실버3
유형: 슬라이딩 윈도우 + 누적합
시간: 10분
- 구상 15:25 ~ 15:30 (5분)
- 디버깅 15:45 ~ 15:50 (5분)

풀이
- start, end 범위만 잘 맞으면 되..는게 아냐?
  - 누적합이래요.. -> 해보고 안되면 누적합 등의 방법 생각하기




'''