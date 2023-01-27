# 1541. 잃어버린 괄호

def calc(eq):
    res = 0
    try:
        res = eval(eq)
    except:
        eq = eq.split('+')
        for e in eq:
            res += int(e)
    return res

equation = input().split('-')
total = calc(equation[0])

for eq in equation[1:]:
    total -= calc(eq)

print(total)