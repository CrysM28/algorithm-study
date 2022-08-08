# for easy problems

x = int(input())
n = int(input())
price = []
num = []
total = 0

for _ in range(n):
    a,b=map(int, input().split())
    price.append(a)
    num.append(b)

for i in range(n):
    total += price[i]*num[i]

if total == x:
    print("Yes")
else:
    print("No")