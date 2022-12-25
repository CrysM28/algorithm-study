def solution(k, dungeons):
    answer = 0
    n = len(dungeons) 
    visited = [0] * n
    
    
    def dfs(d, cur_hp, num):
        nonlocal answer
        
        if num > answer:
            answer = num

        for i in range(n):
            if visited[i] == 0 and cur_hp >= dungeons[i][0]:
                visited[i] = 1
                dfs(i, cur_hp - dungeons[i][1], num+1)
                visited[i] = 0
        

    dfs(0, k, 0)
    return answer