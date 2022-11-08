def solution(key, lock):

    # 크기
    n = len(lock)
    m = len(key)

    # 자물쇠 패딩
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 중앙에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]


        
    print(new_lock)

    # 열쇠 끼우기 - 4방향 회전 시켜서 확인
    rotated = key[:]
    for _ in range(4):
        
        rotated = list(zip(*rotated[::-1]))
        #print(i, rotated)

        # 자물쇠 확인
        for i in range(n*2):
            for j in range(n*2):

                # 실험용 자물쇠 
                test_lock = new_lock[:]
                # print("before")
                # print(*test_lock, sep="\n")
                # print("after")

                # 열쇠 끼우기
                for x in range(m):
                    for y in range(m):
                        test_lock[x+i][y+j] += key[x][y]

                # print(*test_lock, sep="\n")




                # print("==")




    answer = True

    return answer


print(
    solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
             [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
'''
배열 회전 팁

rotated = list(zip(*original[::-1]))


'''