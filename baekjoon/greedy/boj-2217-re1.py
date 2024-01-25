# 2217. 로프

n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort()

ans = 0
weight = 0

for i in range(n):
    weight = rope[i] * (n-i)
    if (ans < weight):
        ans = weight
        #print(i, rope[i], ans)

print(ans)


'''
난이도: 실버4
유형: 그리디
시간: 15:15 ~ 20 (5분)

풀이
- 최소 하중만큼 여러 개 드는게 어떤게 제일 많이 들 수 있는지 쭉 돌면서 비교
- for문 한번만 돌면 되므로 O(N)

'''