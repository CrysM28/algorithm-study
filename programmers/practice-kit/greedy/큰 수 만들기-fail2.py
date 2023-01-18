# 앞 2개 묶음에서 최소값 삭제하는 것을 k번 반복
## 계속 맨 앞에는 큰 값만 남게 되므로 최적해 찾을 수 있음

# 인터넷 찬스 -> 스택 할용해보기

def solution(number, k):

    stack = list()
    stack.append(number[0])
    idx = 1

    while k != 0 and idx < len(number):
        curr = stack.pop()

        # stack의 마지막 값보다 작으면 stack에 push
        if number[idx] <= curr:
            stack.append(curr)
            stack.append(number[idx])

        # stack의 마지막 값보다 크면 계속 pop하다가
        ## 자기보다 큰 값이 나오면 or 스택의 끝까지 가면 push
        else:
            while True:
                tmp = stack.pop()
                k -= 1

                # 숫자 삭제 끝, 남은 거 다 밀어넣기
                if k == 0:
                    for i in range(idx, len(number)):
                        stack.append(number[i])
                    break

                # 자기보다 큰 값
                if tmp > number[idx]:
                    print("tmp, num[i]", tmp, number[idx])
                    stack.append(tmp)
                    stack.append(number[idx])
                    break
                
                # 스택의 끝
                elif not stack:
                    stack.append(number[idx])
                    break


        print(stack)

        idx += 1
        #k -= 1


    return number

#print(solution("21613", 4))
print(solution("4177252841", 4))
#print(solution("8888844", 2))
#print(solution("88982199333", 4))
#print(solution("87654321", 3))

