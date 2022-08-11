# 15829. Hashing
l = int(input())
strs = input()
sum = 0

for i, s in enumerate(strs):
    ai = ord(s) - ord('a') + 1
    sum += (ai * 31**i)

print(sum % 1234567891)