class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plusOne(curr, i):
            origin = curr[i]
            if origin == "9":
                new = "0"
            else:
                new = chr(ord(origin) + 1)
            plus = ""
            for k in range(4):
                if k != i:
                    plus += curr[k]
                else:
                    plus += new 
            return plus
        def minusOne(curr, i):
            origin = curr[i]
            if origin == "0":
                new = "9"
            else:
                new = chr(ord(origin) - 1)
            minus = ""
            for k in range(4):
                if k != i:
                    minus += curr[k]
                else:
                    minus += new
            return minus
        deads = set(deadends)
        nums = "0000"
        q = [nums]
        visited = set([])
        res = 0
        while q:
            size = len(q)
            # print(q)
            for i in range(size):
                curr = q.pop(0)
                if curr in deads:
                    continue
                if curr == target:
                    return res
                if curr in visited:
                    continue
                visited.add(curr)
                for i in range(4):
                    plus = plusOne(curr, i)
                    print(plus)
                    if plus not in visited and plus not in deads:
                        q.append(plus)
                for i in range(4):
                    minus = minusOne(curr, i)
                    if minus not in visited and minus not in deads:
                        q.append(minus)
            res += 1
        return -1

