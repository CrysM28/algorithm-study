# 16637. 괄호 추가하기

n = int(input())
eq = input()

result = eval(eq)

print(eq)
print(result)

for i in range(1,n,2):
    ops = eq[i]
    new_eq = eq
    
    new_eq = eq[:i-1] + '(' + eq[i-1:i+2] + ')' + eq[i+2:]
    print(new_eq)
