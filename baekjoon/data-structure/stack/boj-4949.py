# 4949. 균형잡힌 세상

def check_parenthesis(str_):
    stack = []  # 괄호 카운팅

    for s in str_:
        if s == "(" or s == "[":
            stack.append(s)

        elif s == ")" or s == "]":
            if not stack: return "no"  # 왼쪽이 없으므로 짝 안 맞음

            st = stack.pop()
            if st == "(" and s == ")": pass
            elif st == "[" and s == "]": pass
            else: return "no"

    # 마지막에 스택이 안 비어있으면 짝 안 맞는 것
    if stack: return "no"
    else: return "yes"


while True:
    str_input = input()
    if str_input == ".": break
    print(check_parenthesis(str_input))