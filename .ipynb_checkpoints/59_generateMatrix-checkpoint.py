# 注意到现象：每一次都是在矩阵的四个边界上放置元素，然后放置满了之后边界向内收缩
# 例如，先在上边界那一行从左到右放置元素，放置满了之后，在右边界那一列放置元素
# 但是要注意，放置完之后，上边界下移一行，右边界左移一行
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0] * n for _ in range(n)]
        up = 0
        down = n - 1
        left = 0
        right = n - 1
        x = 0
        y = 0
        num = 1
        # for i in range(1, n * n + 1):
        while num <= n * n:
            # 在循环里边按照四条边的顺序依次放就行：上、右、下、左
            # x = left
            # y = up
            x = up
            y = left
            if right < left: continue
            for i in range(right - left + 1):
                m[x][y] = num
                num += 1
                y += 1
            up += 1
            x = up
            y = right
            if down < up : continue
            for i in range(down - up + 1):
                m[x][y] = num
                num += 1
                x += 1
            right -= 1
            x = down
            y = right
            if right < left: continue
            for i in range(right - left + 1):
                m[x][y] = num
                num += 1
                y -= 1
            down -= 1
            x = down 
            y = left
            if down < up : continue
            for i in range(down - up + 1):
                m[x][y] = num
                num += 1
                x -= 1
            left += 1
        return m


            # num += 1
            # m[x][y] = i
            # if x >= left and x <= right and y >= up and y <= down:
            #     m[x][y] = num
            #     num += 1
            #     x += 1 
            # if x > right:
            #     x = x - 1


