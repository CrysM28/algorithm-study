
h, m, s = map(int, input().split())
cook = int(input())

t = h*60*60 + m*60 + s + cook

h = t // 3600
t -= h * 3600
if h > 23:
    h = (h%24)


m = t // 60
t -= m * 60

s = t

print(h, m, s)