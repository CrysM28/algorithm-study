zigzag = {"00":0, "01":1, "10":2, "11":3}

def Reduce(n, row, col):
    nsq = 2**n
    i,j = row//(nsq) , col//(nsq)
    row , col = row % nsq, col % nsq
    ret = zigzag[str(i)+str(j)] * nsq * nsq
    return ret, row, col, n

ans = 0
n, r, c = map(int, input().split())
while n > 0:
    ret,r,c,n = Reduce(n-1, r,c)
    ans += ret
    if r==0 and c==0:
        break
print(ans)