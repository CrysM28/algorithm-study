# 1074. Z

def div(n, i, j):
    global cnt

    def quadrant(half):
        nonlocal i, j

        if i < half:
            if j < half:
                return 0
            else:
                j -= half
                return 1
        else:
            if j < half:
                i -= half
                return 2
            else:
                i -= half
                j -= half
                return 3
    

    multiplier = 2**(2*(n-1))
    q = quadrant(2**(n-1))
    cnt += multiplier * q
    
    # print("lu", multiplier)
    # print("quad", q)
    # print("sum", cnt)

    if n > 1:
        div(n-1, i, j)

    return cnt



N, r, c = map(int, input().split())

cnt = 0
div(N, r, c)
print(cnt)
