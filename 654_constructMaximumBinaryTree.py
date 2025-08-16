# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # search_index = dict()
        # sorted_nums = sorted(nums, key = lambda x: -x)
        # for i, num in enumerate(sorted_nums):
        #     search_index[num] = i
        # root = TreeNode(val = sorted_nums[0])
        # split = search_index[sorted_nums[0]]

        def helper(nums, l, r):
            # if len(nums) == 0:
                # return 
            if l > r:
                return
            max_val = -float("inf")
            max_index = 0
            # for i, num in enumerate(nums[l:r+1]):
            #     if max_val < num:
            #         max_index = i
            i = l
            while i <= r:
                if max_val < nums[i]:
                    max_index = i
                    max_val = nums[i]
                i += 1
            root = TreeNode(val = nums[max_index])
            left = helper(nums, l, max_index - 1)
            right = helper(nums, max_index + 1, r)
            root.left = left
            root.right = right
            # left = helper(root, nums[0:split], search_index[max(nums[0:split])])
            return root
        return helper(nums, 0, len(nums) - 1)
