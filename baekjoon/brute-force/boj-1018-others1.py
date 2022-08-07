import sys
N,M=map(int,input().split())
bf,wf = [],[]
x = True
for _ in range(N):
    s = sys.stdin.readline().rstrip()
    y = True
    B,W = [],[]
    for c in s:
        if (c=='B' and y) or (c=='W' and not y):
            B.append(0)
            W.append(1)
        else:
            B.append(1)
            W.append(0)
        y = not y
    aB,aW = [],[]
    for i in range(M-7):
        aB.append(sum(B[i:i+8]))
        aW.append(sum(W[i:i+8]))
    if x:
        bf.append(aB)
        wf.append(aW)
    else:
        bf.append(aW)
        wf.append(aB)
    x = not x

BX = [[0]*(M-7) for _ in range(N-7)]
WX = [[0]*(M-7) for _ in range(N-7)]
for i in range(M-7):
    for j in range(N-7):
        BX[j][i] = sum([bf[j+k][i]for k in range(8)])
        WX[j][i] = sum([wf[j+k][i]for k in range(8)])
        
MBX = map(min,BX)
MWX = map(min,WX)
print(min(min(MBX),min(MWX)))