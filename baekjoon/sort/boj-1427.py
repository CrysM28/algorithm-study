# 1427. 소트인사이드

num = list(map(int, input()))
num.sort(reverse=True)
print(*num,sep='')