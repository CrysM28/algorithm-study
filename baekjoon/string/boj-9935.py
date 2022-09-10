# 9935. 문자열 폭발

s = input()  # 문자열
e = input()  # 폭발

word = []  # 최종 글자
stack = []  # 임시 스택

max_e = len(e) - 1
idx_e = 0


# 한 글자씩 확인 (O(n))
for ss in s:
    print("===")
    print(word, stack, idx_e)
    word.append(ss)

    # 폭발 문자면
    if ss == e[idx_e]:
        stack.append(idx_e)

        # 폭발 문자열 완성되면 삭제
        if idx_e == max_e:
            # 순서대로 있는지부터 확인
            in_order = True
            for i in range(idx_e + 1):
                if stack[-(i+1)] != idx_e-i:
                    in_order = False

            # 순서대로 들어있으면 폭발 문자열이 맞음
            if in_order:
                for _ in range(idx_e + 1):
                    word.pop()
                    stack.pop()
                # 중복된 폭발 문자면
                if stack:
                    idx_e = stack[-1] + 1
                else:
                    idx_e = 0
            # 그렇지 않으면 폭발 문자열이 아님
            else:
                idx_e = 0
                stack = [] 

        else:
            idx_e += 1

    # 폭발 문자 (중복)
    elif idx_e != 0 and ss == e[idx_e - 1]:
        stack.append(idx_e-1)

    # 새로 시작하는 폭발 문자
    elif ss == e[0]:
        stack.append(0)
        idx_e = 1

    # 일반 문자
    else:
        idx_e = 0
        stack = []  # 폭발문자 연속 X면 스택 초기화

    print(word, stack, idx_e)


# 결과 출력
if len(word) == 0:
    print("FRULA")
else:
    print(''.join(word))