# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(  head: Optional[ListNode], nums:  [int]) -> int:
        p = head
        hashset = set(nums)
        ans = 0
        while p != None:
            # if (p.next is not None and  p.next.val not in hashset) or p.next == None:
            # if (p.next is not None and p.next.val not in hashset):
            if (p.val in hashset) and (p.next is None or (p.next is not None and p.next.val not in hashset)): 
            # 注意条件：p在
                ans += 1  
            p = p.next
        return ans
    
# 上边这种解法不好，下边这种解法更好：
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums_set = set(nums)
        p = head
        count = 0
        while p:
            if p.val in nums_set:
                while p and p.val in nums_set :   # 表示走过一段连通分量
                    p = p.next
                count += 1
            else:
                while p and  p.val not in nums_set:  # 表示走过一段连通分量（把不在nums中的看成连通分量）
                    p = p.next
        return count