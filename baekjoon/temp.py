
i = 1
while True:
    n = int(input())

    if n == 0:
        break

    songs = []
    for _ in range(n):
        songs.append(input())

    songs.sort()

    print(i)
    print(*songs, sep='\n')

    i += 1