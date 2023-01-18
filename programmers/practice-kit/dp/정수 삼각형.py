def solution(triangle):
    n = len(triangle)

    for i in range(1, n):
        t = triangle[i]
        
        for j in range(i+1):
            if j == 0:
                t[j] += triangle[i-1][0]
            elif j == i:
                t[j] += triangle[i-1][i-1]
            else:
                t[j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    answer = max(triangle[-1])
    return answer