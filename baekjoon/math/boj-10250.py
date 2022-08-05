# ACM 호텔

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    rooms = []

    for j in range(1, w + 1):
        for i in range(1, h + 1):
            rooms.append([i, j])

    floor_n = str(rooms[n - 1][0])
    room_n = str(rooms[n - 1][1]).zfill(2)
    print(floor_n + room_n)

    ### others
    #     print(100 * (N % H) + (N // H)+ (100 * H if N % H == 0 else 1))