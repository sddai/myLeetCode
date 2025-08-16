# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 【核心观点】一个子树内部的最大路径和 = 左子树提供的最大路径和 + 根节点值 + 右子树提供的最大路径和
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def find_max(root):
            if not root:
                return 0
            # case1 = root.val + find_max(root.left) + find_max(root.right) # 错了：
            # 注意如果通过find_max地柜过程传上来的值是负数，则不加入，也就是取一个max(0, ...)
            l = find_max(root.left)
            r = find_max(root.right)
            # case1 = root.val + max(0, find_max(root.left)) + max(0, find_max(root.right))
            # case2 = root.val + max(0, find_max(root.left), find_max(root.right)) # 这种写法重复计算递归函数find_max，会超时
            case1 = root.val + max(0, l) + max(0, r)
            case2 = root.val + max(0, l, r)
            nonlocal curr_sum
            curr_sum = max(curr_sum, case1, case2)
            return case2
        curr_sum = -float("inf")
        find_max(root)
        return curr_sum
    
'''来自题解中的另一种解释方法：（代码类似，理解思路更加直接，同687）
这种解法同687，每次递归返回的是左右子树中比较大的那一个，但是每次用于更新max_val的是左右子树返回值的和

const maxPathSum = (root) => {
    let maxSum = Number.MIN_SAFE_INTEGER; // 最大路径和

    const dfs = (root) => {
        if (root == null) { // 遍历到null节点，收益0
           return 0;
        }
        const left = dfs(root.left);   // 左子树提供的最大路径和
        const right = dfs(root.right); // 右子树提供的最大路径和

        const innerMaxSum = left + root.val + right; // 当前子树内部的最大路径和
        maxSum = Math.max(maxSum, innerMaxSum);      // 挑战最大纪录

        const outputMaxSum = root.val + Math.max(0, left, right); // 当前子树对外提供的最大和

        // 如果对外提供的路径和为负，直接返回0。否则正常返回
        return outputMaxSum < 0 ? 0 : outputMaxSum;
    };

    dfs(root);  // 递归的入口

    return maxSum; 
};

作者：笨猪爆破组
【推荐】链接：https://leetcode.cn/problems/binary-tree-maximum-path-sum/solutions/297276/shou-hui-tu-jie-hen-you-ya-de-yi-dao-dfsti-by-hyj8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''