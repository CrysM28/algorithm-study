def solution(k, dungeons):
    answer = 0
    n = len(dungeons) 
    visited = [0] * n
    
    
    def dfs(d, cur_hp, num):
        nonlocal answer
        
        visited[d] = 1
        cur_hp -= dungeons[d][1]

        for i in range(n):
            if visited[i] == 0 and cur_hp >= dungeons[i][0]:
                dfs(i, cur_hp, num+1)
                visited[i] = 0
        
        answer = max(answer, num)
        

    dfs(0, k, 1)
    return answer