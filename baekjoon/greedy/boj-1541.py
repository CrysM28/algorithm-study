# 1541. 잃어버린 괄호

equation = input()
min_num = 100

for e in equation:
    if not e.isdigit():
        print(e)
ans = eval(equation)

print(ans)