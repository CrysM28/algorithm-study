# 한수
hansu = 0
n = int(input())

# 1~n 검사
for i in range(1, n + 1):
    cur_num = str(i)

    # 한두자리수는 무조건 한수
    if i < 100:
        hansu += 1
        continue

    # 세자리수 이상부터 계산
    cha = int(cur_num[0]) - int(cur_num[1])
    for x in range(1, len(cur_num)):
        if (int(cur_num[x - 1]) - int(cur_num[x])) != cha:
            break
    else:  # break 없이 끝까지 조건 통과시 한수
        hansu += 1

print(hansu)