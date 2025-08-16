class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 直接每隔一层倒置一层，不用每次判断奇偶
        res = []
        while label:
            res.append(label)
            label = label // 2
        res = res[::-1]
        n = len(res)
        for i in range(n - 2, -1, -2):
            original = res[i]
            start = 2 ** i
            end = start * 2
            reversed_ = end - 1 - (original - start)
            res[i] = reversed_
        return res
        # 超时：超时原因是多了判断奇偶的过程
        # def find_layer(label):   # 这里增加了时间复杂度
        #     layer = 0
        #     while label:
        #         label = label // 2
        #         layer += 1
        #     return layer
        # def get_list(label, layer):
        #     size = 2 ** (layer - 1)
        #     start = size
        #     end = size * 2 - 1
        #     return [start, end]
        # def parent(label):
        #     layer = find_layer(label)
        #     if layer % 2 == 1:
        #         # 当前层是正序，上一层是倒序，先按当前label恢复上层index再倒序
        #         start, end = get_list(label, layer)
        #         index = label // 2 - start   # 表明需要返回的是上一行的第index个数（0开始计数）
        #         res = (start - 1) - index - 1
        #     else:
        #         start, end = get_list(label, layer)
        #         # 当前层是倒序，上一层是正序，先恢复当前序号再计算上层序号
        #         index = start + end - label
        #         res = index // 2
        #     return res
        # ans = []
        # while label:
        #     # ans.append(parent(label))
        #     ans.append(label)
        #     label = parent(label)
        # return ans[::-1]

