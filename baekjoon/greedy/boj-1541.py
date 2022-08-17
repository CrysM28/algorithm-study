# 1541. 잃어버린 괄호
# - 기준으로 묶어서 빼면 최소값이 나옴

equation = input().split('-')
answer = 0

for i, e in enumerate(equation):
    if i == 0:
        for ee in e.split('+'):
            answer += int(ee)
    else:
        for ee in e.split('+'):
            answer -= int(ee)

print(answer)