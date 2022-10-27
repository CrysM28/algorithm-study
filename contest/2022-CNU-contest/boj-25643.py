# 25643. 문자열 탑 쌓기

n, m = map(int, input().split())
blocks = [input() for _ in range(n)]

can_tower = True

for i in range(1, n):
    can_put = False
    cur_block = blocks[i]
    prev_block = blocks[i-1]

    for j in range(m):
        cur_word = cur_block[:j+1]
        prev_word = prev_block[m-j-1:]

        if cur_word == prev_word:
            can_put = True
            break
    else:
        for j in range(m):
            cur_word = cur_block[m-j-1:]
            prev_word = prev_block[:j+1]

            if cur_word == prev_word:
                can_put = True
                break

    if not can_put:
        can_tower = False
        break

if can_tower:
    print(1)
else:
    print(0)

