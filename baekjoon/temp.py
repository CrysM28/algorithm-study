# for easy problems

while True:
    a,b,c = input().split()
    
    if a == '#' and b==c=='0':
        break
    if int(b)>=17 or int(c) >=80:
        print(a, "Senior")
    else:
        print(a, "Junior")

