# 6198. 옥상 정원 꾸미기


N = int(input())
building = []
for _ in range(N):
    building.append(int(input()))


ans = 0
stack = [(building[-1], 0)]

for i in range(N-2, -1, -1):
    cnt = 0

    while stack and building[i] > stack[-1][0]:
        h, c = stack.pop()
        cnt += c + 1
        ans += c
    
    stack.append((building[i], cnt))

while stack:
    h, c = stack.pop()
    ans += c

print(ans)


'''
난이도: 골드5
유형: 스택
시간: 40분
- 구상 및 구현 14:00 ~ 14:40


풀이
- N개의 빌딩 오른쪽으로 보며 낮은 빌딩의 층고만 확인
- 스택인 걸 보고 시작했는데 이런식으로 한쪽만 보고 세는건 거의 스택 문제인듯

- 역으로 생각하기.. 내가 볼 수 있는 개수를 셀 필요 없이
  걔를 몇 번을 보는가를 세면 되는 거와 같은 원리임

'''