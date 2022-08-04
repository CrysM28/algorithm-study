# 크로아티아 알파벳

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

for c in croatia:
#    while c in word:                       # 하나씩 볼 필요 없음
#        word = word.replace(c, "0", 1)
    word = word.replace(c, "0")

print(len(word))