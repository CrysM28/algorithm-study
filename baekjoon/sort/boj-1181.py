# 1181. 단어 정렬

n = int(input())

## 한줄로 줄이기
words = sorted(list(set(input() for _ in range(n))))    # set으로 중복제거
# words = list(set(input() for _ in range(n)))    # set으로 중복제거
# words.sort()

words.sort(key = len)
print(*words, sep="\n")