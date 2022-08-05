# 손익분기점
## while로 돌리면 시간초과 뜨기 때문에 식으로 정리해서 푸는 게 빠르고 좋다~

a, b, c = map(int, input().split())
if (c - b) <= 0: print(-1)
else: print((a // (c - b)) + 1)
