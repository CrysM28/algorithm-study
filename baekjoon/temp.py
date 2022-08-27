# for easy problems

n = int(input())

for i in range(1,n):
    s = "*"*i
    print(s.rjust(n))

for i in range(n,0,-1):
    s = "*"*i
    print(s.rjust(n))
