# 2805. 나무 자르기

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)
ans = 0

while start <= end:
    height = (start+end) // 2

    sg_tree = 0
    for tree in trees:
        if tree > height:
            sg_tree += tree - height

    # 더 높이 잘라도 되겠다
    if sg_tree >= m:
        ans = height
        start = height + 1
    
    # 더 낮게 잘라야겠다
    else:
        end = height - 1

print(ans)
