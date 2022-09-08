# 1107. 리모컨

target = int(input())
broken_num = int(input())
if broken_num:
    broken = set(input().split())
else:
    broken = set()

# 최대값: +-만 누른 경우로 초기화
press = abs(100 - target)

# 큰 수에서 작은 수 내려오는 경우도 고려해서 가능한 채널의 2배로
for num in range(1000001):
    # 앞에서부터 있는 숫자 누르기
    for n in str(num):
        # 고장난 숫자 있으면 바로 못 가는 채널
        if n in broken:
            break
    # 고장난 숫자 없이 누를 수 있으면 차이 구하기 (len은 누르는 자릿수만큼)
    else:
        press = min(press, abs(num - target) + len(str(num)))

print(press)