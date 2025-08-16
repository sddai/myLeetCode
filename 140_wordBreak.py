# 此题几乎一遍通过
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(s, i, path):
            nonlocal res   # 可加可不加 
            if i == n:
                res.append(" ".join(path[:]))
                return 
            for j in range(i + 1, n + 1):
                if s[i:j] in word_dict:
                    path.append(s[i:j])
                    dfs(s, j, path)
                    path.pop()
        n = len(s)
        path = []
        res = []
        word_dict = set(wordDict)
        dfs(s, 0, path)
        return res