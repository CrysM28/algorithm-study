# 9184. 신나는 함수 실행


def w(a,b,c):
    print("i am ", a,b, c)
    if a <= 0 or b <= 0 or c <=0:
        return 1
    
    elif a > 20 or b > 20 or c >20:
        return w(20,20,20)
    
    elif a<b<c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    else:
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)


while True:
    a, b, c = map(int, input().split())

    if a == b == c == -1:
        break

    answer = w(a,b,c)

    print(answer)
