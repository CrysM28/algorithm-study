# 1918. 후위 표기식
## 굳이 괄호 같은거에 집착할 필요없이 결과만 맞으면 됨...
equation = list(input())

##### 괄호치기
# +, - 단위로 묶기
eq = equation[:]
for e in equation:
    if e == '+' or e == '-':
        # 왼쪽
        i = eq.index(e)
        while i > 0:
            i -= 1
            if eq[i] == '+' or eq[i] == '-':
                i = i + 1
                break
        eq.insert(i, '(')

        # 오른쪽
        i = eq.index(e)
        while i < len(eq) - 1:
            i += 1
            if eq[i] == '+' or eq[i] == '-':
                i = i - 1
                break
        eq.insert(i + 1, ')')

# *, / 



equation = eq[:]

eq = ''.join(eq)
print(eq)

##### 후위연산자 변환
# 연산자 보관 스택
stack = []





# # 괄호치기
# def parenthesis():
#     # 왼쪽 괄호
#     i = eq.index(e)
#     if eq[i - 1].isalpha():
#         eq.insert(i - 1, '(')
#     else:
#         while eq[i] != '(':
#             i -= 1
#         eq.insert(i, '(')

#     # 오른쪽 괄호
#     i = eq.index(e)
#     if eq[i + 1].isalpha():
#         eq.insert(i + 2, ')')
#     else:
#         while eq[i] != ')':
#             i += 1
#         eq.insert(i + 1, ')')

# equation = list(input())

# # 괄호치기: 우선순위 높은 *, / 부터
# eq = equation[:]
# for e in equation:
#     if e == '*' or e == '/':
#         parenthesis()
# equation = eq[:]

# print(''.join(eq))

# # 괄호치기: 그 다음 우선순위 +, -
# eq = equation[:]
# for e in equation:
#     if e == '+' or e == '-':
#         parenthesis()

# eq = ''.join(eq)
# print(eq)

# # 연산자 보관 스택
# stack = []
