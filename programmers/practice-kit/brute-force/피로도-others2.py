def solution(k, dungeons):
    max_cnt = 0
    N = len(dungeons)
    visited = set()

    def dfs(curr_k, cnt):
        global max_cnt
        max_cnt = max(max_cnt, cnt)

        for i in range(N):
            # 현재 던전을 방문한 적이 없고, 현재피로도 >= 최소피로도 이면 진행
            if i not in visited and curr_k >= dungeons[i][0]:
                visited.add(i)
                dfs(curr_k - dungeons[i][1], cnt + 1)
                visited.remove(i)

    dfs(k, 0)
    return max_cnt


"""
- DFS 완전탐색
"""