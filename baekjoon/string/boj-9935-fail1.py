# 9935. 문자열 폭발
## 시간초과 -> in 연산 때문일듯


s = input() # 문자열
e = input() # 폭발

while e in s:
    s = s.replace(e, "")

if s == "":
    print("FRULA")
else:
    print(s)
    