N, M = map(int, input().split())
T = list(map(int, input().split()))
if T[0]:
    T = set(T[1:])
    party = [set(list(map(int, input().split()))[1:]) for i in range(M)]
    br = True
    visit = [True] * M
    while br:
        br = False
        for i, x in enumerate(party):
            if x.intersection(T) and visit[i]:
                for k in x:
                    T.add(k)
                visit[i] = False
                br = True
    print(sum(visit))
else:
    print(M)