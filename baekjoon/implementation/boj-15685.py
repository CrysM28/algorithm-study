# 15685. 드래곤 커브

di = (0, 1, 0 , -1)
dj = (1, 0, -1, 0)

N = int(input())
grid = [[False] * 100 for _ in range(100)]

# x, y, d, g (편의를 위해 반대로 저장: x=j, y=i라서)
dragon_curves = []
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon_curves.append([y, x, d, g])

def get_dragon_curve(i, j, dir, cur_gen):
    print(cur_gen)
    new_dir = (dir-1)%4
    ni = i+di[dir]
    nj = j+dj[dir]

    if cur_gen == 0:
        dc_pt.append([ni, nj])
        return [ni, nj]


    end_pt = get_dragon_curve(i, j, dir, cur_gen-1)
    print(end_pt)
    end_pt = get_dragon_curve(end_pt[0], end_pt[1], new_dir, cur_gen-1)
    print(end_pt)
    #get_dragon_curve(ni, nj, dir, cur_gen-1)


    return end_pt


i, j, dir, gen = dragon_curves[0]

dc_pt = [[i, j]]
get_dragon_curve(i, j, dir, gen)

print(dc_pt)