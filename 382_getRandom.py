# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.rand = random.Random(0)


    def getRandom(self) -> int:
        p = self.head
        i = 0
        res = 0
        while p != None:
            i += 1
            if 0 == self.rand.randint(0, i - 1):
                res = p.val # ·这个数是在不断被刷新的，第i个数有1/i的概率被刷新成当前值
            p = p.next
        return res



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()