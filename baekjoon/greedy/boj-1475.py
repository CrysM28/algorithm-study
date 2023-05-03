# 1475. 방 번호

n = list(map(int, input()))

cnt = [0] * 10
for number in n:
    cnt[number] += 1

six_and_nine = cnt[6] + cnt[9]
half = six_and_nine // 2
if six_and_nine % 2 == 0:
    cnt[6], cnt[9] = half, half
else:
    cnt[6], cnt[9] = half, half + 1

plastic = max(cnt)
print(plastic)
