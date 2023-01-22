# 2292. 벌집

n = int(input())

compare = 2
room = 1

while True:
    if n < compare:
        break
    else:
        compare += 6 * room
        room += 1

print(room)
