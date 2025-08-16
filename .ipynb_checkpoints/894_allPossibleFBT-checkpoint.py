'''
动态规划解法：
本题的思想是，dp是一个二维数组，dp[n]的含义是———将n各节点全部分配给左右子树，树的所有可能情况

每次把这n个节点分给左右子树，例如左子树被分到了i个节点，root占用1个节点，则右子树占用n-i-1个节点

递归的思路解析：
//我们知道一共有N个结点，root占了1个结点，左子树可能有1，3，5，..，N-2个结点（不会是0，因为左子树为0，满足条件的右子树就需要也是0，递归停止；也不会是N，因为都分配给左子树，右子树没有可以分配的节点了，不平衡）
//对应的，右子树可能有N-2，..，5，3，1个结点
//那么，我们可以用一个循环，找到所有可能的左右子树的可能的数量的情况，把root放进列表里

函数（或者说dp）的含义：
allPossibleFBT(i)返回了一个列表，它存放着当结点数为i时，所有满足条件的树的root的集合
（！！！这里要注意，函数返回的并不是一个数组或者列表，而是一个由根节点组成的list）
虽然题目中给出的result是一个list，但是注意看函数头，返回的其实只有一个根结点（代表一种可能的结果），7中可能结果就返回7个根结点组成的list

【动态规划的思路解析】：
/*动态规划（总体思路和记忆化递归类似）
    dp[i]代表节点个数为i个的真二叉树（的根结点）列表，每个根节点已经按要求构造好了一个可能的真二叉树
    状态转移方程：
        类似于乘法原理，左边x个，右边n-x-1个，然后组合
    初始化：dp[1] = {new TreeNode(0)};
    遍历顺序：dp[i]用到的一定是比i小的dp数组，所以自然是顺序遍历
*/

'''
# 如下代码已AC：
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def allPossibleFBT(n: int) -> [Optional[TreeNode]]:
    if n % 2 == 0:
        return []
    # if n == 1:
    #     return [[0, ]]
    # if n == 3:
    #     return [[0, 0, 0]]
    dp = [[] for _ in range(n+1)]
    # dp[1] = [[0, ]]
    # dp[3] = [[0, 0, 0]]  # 这里不要受到题目描述的误导，本题返回的并不是节点的序列，而是根节点组成的list，换句话说，这里的一个[[0, 0, 0]]只需要返回一个构造好的树的根结点就可以，即只需要返回[TreeNode(0, 0, 0), ]

    dp[1].append(TreeNode(0))
    for i in range(3, n+1, 2):   # 遍历的i是：总的节点数
        for j in range(1, i, 2): # 遍历的j是：所有可能的左子树的节点个数   # 这里是i不是i-1
            # 所有可能的右子树节点个数是：k = n - 1 - j
            for left in dp[j]:   # 确定了左右子树的节点数之后，开始从j和k中取出所有可能的根结点
                for right in dp[i - 1 - j]:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right   # 这棵树是随着dp[i]中i的增大而逐渐构造起来的，i表示一共有i个节点的符合条件的树（dp里边记录了这样的树的根节点）
                    dp[i].append(root)
    return dp[n]