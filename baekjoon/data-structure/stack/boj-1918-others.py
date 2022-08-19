import sys

# 수식기호 넣는 곳
stack = list()

# 수식
result = ""
sen = list(sys.stdin.readline().rstrip())

# 과정
# 알파벳 -> push, 수식기호 : 낮은 우선순위가 나오면 출력(다음 알파벳을 위해), 나머지 수식기호 다 붙이기
# 우선순위 : ( => +,- => *,/ => )
for x in sen:
    if x.isalpha():
        result += x
    elif x == '(':
        stack.append(x)
    elif x == '*' or x == '/':
        # * 나 /가 있으면 빼기 -> 다른것(+,-)이면 계속
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            result += stack.pop()
        stack.append(x)
    elif x == '+' or x == '-':
        # ( 나올 때까지 빼기
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(x)
    elif x == ')':
        #여는 괄호 나올 때까지 붙이기
        while stack and stack[-1] != '(':
            result += stack.pop()
        #여는 괄호 빼기
        stack.pop()

while stack:
    result += stack.pop()
print(result)