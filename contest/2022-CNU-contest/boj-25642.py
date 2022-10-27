# 25642. 젓가락 게임

a, b = map(int, input().split())

yt_turn = True
yt_win = True

while True:
    if yt_turn:
        b += a
        yt_turn = False
    else:
        a += b
        yt_turn = True
    
    if a > 5:
        yt_win = False
        break
    elif b > 5:
        yt_win = True
        break

if yt_win:
    print("yt")
else:
    print("yj")