n = input()
if len(n) == 1:
    n = "0" + n

initial_n = n
cycle = 0

while True: 
    a = n[0]
    b = n[1]
    sum1 = str(int(a)+int(b))

    n = b + sum1[-1]
    cycle += 1

    if n == initial_n:
        print(cycle)
        break