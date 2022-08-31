# 2579. 계단 오르기
## dp 말고 정렬해서 풀어보려고 했는데 예외가 있다

stair = dict()      # key: 몇번째 계단인지, value: 계단 점수
selected = dict()   # 선택된 계단

n = int(input())
for i in range(n):
    stair[i] = int(input())

# 가장 마지막 계단은 필수로
selected[n-1] = stair[n-1]
del stair[n-1]

# 점수 내림차순 정렬
stair = dict(sorted(stair.items(), key = lambda item: item[1], reverse = True))

print(stair, selected)

# 높은 점수 순으로 뽑기
for s in stair:
    # 3개 연속이면 안 됨
    if (s-1 in selected and s+1 in selected) or\
        (s-1 in selected and s-2 in selected) or\
        (s+1 in selected and s+2 in selected):
        continue

    selected[s] = stair[s]

print(selected)

total = 0
for v in selected.values():
    total += v
print(total)