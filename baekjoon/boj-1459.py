# 1459. 걷기

x, y, w, s = map(int, input().split())
dist = 0

if w*2 < s:
    dist = (x*w) + (y*w)
else:
    if x < y:
        left = y-x
        dist = (x*s) 
    else:
        left = x-y
        dist = (y*s) 

    if w > s:
        dist += (left//2)*2 * s + (left%2)*w
    else:
        dist += left * w




print(dist)