# 25634. 전구 상태 뒤집기

N = int(input())
brightness = list(map(int, input().split()))
power = list(map(int, input().split()))

max_brightness = 0
start = 200001
end = 200001

for i in range(N):
    if power[i] == 1:
        continue

    change = 0
    swap_val = 0
    idx = 0
    for j in range(i, N):
        bulb_power = power[j]
        bulb_bright = brightness[j]

        if bulb_power != change % 2:
            change += 1
        if change == 3:
            break

        if bulb_power == 0:
            swap_val += bulb_bright
            idx = j

    #print("swapped", swap_val)
    if max_brightness < swap_val:
        max_brightness = swap_val
        start = i
        end = idx

    #print("cur max", max_brightness, start, end)

#print(start, end, max_brightness)

# 전부 켜져 있으면 제일 작은거 하나만 끄기
if start == end == 200001:
    max_brightness = sum(brightness) - min(brightness)

else:
    for i in range(start):
        if power[i] == 1:
            max_brightness += brightness[i]

    for i in range(end+1, N):
        if power[i] == 1:
            max_brightness += brightness[i]


print(max_brightness)
