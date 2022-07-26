sample_mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# Ver1. Conventional way
def rotate_ver1(mat):
    r = len(mat)
    c = len(mat[0])
    result = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            result[j][r - 1 - i] = mat[i][j]
    return result


# Ver2. Pythonic way
def rotate_ver2(mat):
    return list(map(list, zip(*mat[::-1])))


# Result
# Ver1
for row in rotate_ver1(sample_mat):
    print(row)
print()
# Ver2
for row in rotate_ver2(sample_mat):
    print(row)
print()