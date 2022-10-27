# 25635. 자유 이용권

n = int(input())
ticket = list(map(int, input().split()))
ticket.sort()

max_play = 0
while ticket:
    now = ticket.pop()
    print("ticket", ticket)
    print("now", now)

    if ticket and now != 0:
        next = ticket.pop()
        if next < now:
            max_play += next * 2
            now -= next
        else:
            max_play += now * 2
            now = 0
            next -= now
            ticket.append(next)
        

    print(max_play)

max_play += 1