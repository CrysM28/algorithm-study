s, bomb = input(), input()
n, k = len(s), len(bomb)
result = ''
stack = []
for i in range(n):
    stack.append(s[i])
    # i번째 문자가 폭탄 문자열의 마지막 문자가 아닌 경우 무시
    if s[i] != bomb[-1]:
        continue
    # stack 상단에 폭탄 문자열이 있는지 검사
    data = ''.join(stack[-k:])
    if data != bomb:
        continue
    # 폭탄 문자열 제거
    for _ in range(k):
        stack.pop()

result += ''.join(stack)
if not result:
    result = 'FRULA'
print(result)