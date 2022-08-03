# 스택
import sys

stack = list()  # 스택이 될 배열
cmd_num = int(input())  # 주어지는 명령의 수

for _ in range(cmd_num):
    #cmd = input()          # 시간초과 때문에 input 대신 sys 함수 사용
    cmd = sys.stdin.readline().rstrip()

    if cmd == 'pop':
        if len(stack) == 0:
            print("-1")
            continue
        print(stack.pop())

    elif cmd == 'size':
        print(len(stack))

    elif cmd == 'empty':
        if len(stack) == 0:
            print("1")
        else:
            print("0")

    elif cmd == 'top':
        if len(stack) == 0:
            print("-1")
            continue
        pop_val = stack.pop()
        stack.append(pop_val)
        print(pop_val)

    # push 처리 (다른 명령 없다는 전제 있음)
    else:
        tmp, push_num = cmd.split()
        stack.append(push_num)
