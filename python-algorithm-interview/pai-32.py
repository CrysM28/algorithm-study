# L200: Number of Islands
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 주어진 좌표에서 이어진 땅(1) 탐색
        def dfs(i, j):
            # 땅이 아니거나 범위를 벗어나면 종료
            if i<0 or i >= len(grid) or \
                j<0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                return

            grid[i][j] = 0  # 탐색완료 표식

            # 동서남북 재귀탐색
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)     
        
        count = 0  
        # 주어진 grid를 인덱스로 모두 순회
        for i in range(len(grid)):          # m (행) 
            for j in range(len(grid[0])):   # n (열)
                if grid[i][j] == '1':
                    dfs(i,j)    # 1이면 dfs로 이어진 땅 (섬) 확인
                    count += 1  # 탐색을 마치면 섬 하나 탐색 완료한 것

        return count




# Testcase 
#g = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
g = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(g))

