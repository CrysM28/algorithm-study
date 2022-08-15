# 1107. 리모컨
## 다음에 다시 풀기

target_ch = int(input())
broken_button_num = int(input())
broken = set(map(int, input().split()))

alive = list(set([x for x in range(10)]) - broken)
cur_ch = 100
press = 0

if target_ch == cur_ch:
    print("0")

# 큰 수에서 작은 수 내려오는 경우도 생각해서 가능한 채널의 2배로
for n in range(1000001):
    pass



