
N, L, D = map(int, input().split())

time = 0
bell = D
ans = 0

for i in range(N):
    print(i, time, bell)
    time += L

    if bell < time:
        while bell < time:
            bell += D
        #bell -= D
        print("-", time, bell)

        if bell < time+5:
            ans = bell
            break

        time += 5

    else:
        if time <= bell < time+5:
            ans = bell
            print("hear", bell)
            break
        else:
            time += 5
else:
    ans = bell


print(ans)