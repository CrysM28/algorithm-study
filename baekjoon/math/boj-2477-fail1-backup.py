k = int(input())

x, y = [], []
find_small = []
s1, s2 = 0, 0
s_pos_x , s_pos_y = 0, 0
s_len_x, s_len_y = 0, 0

for i in range(6):
    pos, length = map(int, input().split())

    # 동 or 서 (세로 ,y)
    if pos == 1 or pos == 2: 
        y.append(length)  
        if pos != s_pos_y:
            s_pos_y = pos
            s_len_y = length
        else:
            find_small.append([s_pos_y, s_len_y])
            find_small.append([pos, length])

    # 남 or 북 (가로, x)
    else: 
        x.append(length)  
        if pos != s_pos_x:
            s_pos_x = pos
            s_len_x = length
        else:
            find_small.append([s_pos_x, s_len_x])
            find_small.append([pos, length])

print(x,y,find_small,s1,s2)

s1 = find_small[1][1]
s2 = find_small[2][1]



area = (max(x) * max(y)) - (s1 * s2)
print(area * k)
