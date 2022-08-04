# 그룹 단어 체커
import string

n = int(input())
count = 0

for _ in range(n):
    is_group = True
    word = input()

    for a in string.ascii_lowercase:
        prev_index = -1
        if not is_group:
            break

        for i in range(len(word)):
            if not is_group:
                break
            if a == word[i]:
                # 첫 발견 or 연속 인덱스
                if prev_index == -1 or prev_index + 1 == i:
                    prev_index = i
                else:  # 연속 인덱스 아니면 그룹단어 아님
                    is_group = False

    if is_group:
        count += 1

print(count)
