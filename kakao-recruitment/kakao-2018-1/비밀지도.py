# 40 ~ 15: 25 min

def solution(n, arr1, arr2):
    real_map = []
    map1, map2 = [], []

    for i in arr1:
        mylist = list(map(int, str(format(i, 'b'))))
        while len(mylist) < n:         # 남는 자릿수 0 채우기
            mylist.insert(0, 0)
        map1.append(mylist)

    for i in arr2:
        mylist = list(map(int, str(format(i, 'b'))))
        while len(mylist) < n:
            mylist.insert(0, 0)
        map2.append(mylist)

    for i in range(n):
        temp_str = ""
        for j in range(n):
            # OR 연산
            if map1[i][j] | map2[i][j] == 1:
                temp_str += "#"
            else:
                temp_str += " "
        real_map.append(temp_str)

    return real_map


#print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))