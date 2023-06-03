# 10476. 좁은 미술전시관

N, k = map(int, input().split())
gal = []
for _ in range(N):
    gal.append(list(map(int, input().split())))
input()

#print(gal)


dp_left = [[] for _ in range(N)]
dp_right = [[] for _ in range(N)]
dp_all = [[] for _ in range(N)]

dp_left[0] = [[gal[0][0], 1]]
dp_right[0] = [[gal[0][1], 1]]
dp_all[0] = [[gal[0][0]+gal[0][1], 0]]

# print(dp_left)
# print(dp_right)
# print(dp_all)


for i in range(1, N):
    left = gal[i][0]
    right = gal[i][1]
    all = left + right

    for a, closed in dp_all[i-1]:
        dp_all[i].append([a+all, closed])
        if closed+1 <= k:
            dp_left[i].append([a+left, closed+1]) 
            dp_right[i].append([a+right, closed+1]) 

    for l, closed in dp_left[i-1]:
        dp_all[i].append([l+all, closed])
        if closed+1 <= k:
            dp_left[i].append([l+left, closed+1])
     
    for r, closed in dp_right[i-1]:
        dp_all[i].append([r+all, closed])
        if closed+1 <= k:
            dp_right[i].append([r+left, closed+1]) 



print("==")
# print(dp_left)
# print(dp_right)
# print(dp_all)
# print(dp_left[-1])
# print(dp_right[-1])
print(dp_all[-1])


ans = 0
candidates = dp_left[-1] + dp_right[-1] + dp_all[-1]

for val, closed in candidates:
    if closed == k and val > ans:
        ans = val


print(ans)

