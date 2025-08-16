# 此题几乎一遍通过
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        m = len(image)
        n = len(image[0]) if image else 0
        def dfs(image, i, j, visited):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if image[i][j] != original_color:
                return False
            if visited[i][j]: # 一开始落下了这句话
                return False 
            image[i][j] = color
            visited[i][j] = True  # 一开始落下了这句话
            for i, j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                dfs(image, i, j, visited)
        visited = [[False for _ in range(n)] for _ in range(m)]
        dfs(image, sr, sc, visited)
        return image
