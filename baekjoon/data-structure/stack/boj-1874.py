# 1874. 스택 수열


def check_stack():
    num = 1  # 스택에 넣을 숫자
    stack, ops = [], []  # 임시 스택, 연산자 저장 배열

    for i in ints:
        while True:
            # 아직 필요한 숫자 안나옴
            if num < i:
                stack.append(num)
                ops.append("+")
                num += 1

            # 필요한 숫자 찾음 -> 다음 숫자
            elif num == i:
                ops.append("+")
                ops.append("-")
                num += 1
                break

            # 스택에 있는 숫자 체크해야 함
            else:  # num > i
                # 스택에 아무것도 없으면 끝
                if not stack: return "NO"
                popped = stack.pop()

                # 이미 필요한 숫자는 없어진 상태
                if popped < i: return "NO"  

                # 필요한 숫자 나올때까지 pop
                while popped != i:          
                    popped = stack.pop()
                    ops.append("-")

                #if popped == i: 필요한 숫자 찾음 -> 다음 숫자
                ops.append("-")
                break

    return ops


n_input = int(input())
ints = [int(input()) for _ in range(n_input)]  # 만들고자 하는 수열

if check_stack() == "NO":
    print("NO")
else:
    print(*check_stack(), sep="\n")
