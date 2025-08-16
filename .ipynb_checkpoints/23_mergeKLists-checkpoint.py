# 使用直接线性新建第三个链表暂存中间结果，会超时
# 解决方案：二叉堆
# 注意处理特殊情况: lists = [[],[]] # （需要判断head是否为空 if head: ）
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        ListNode.__lt__ = lambda x, other: x.val < other.val
        for head in lists:
            if head: heapq.heappush(q, head)
        dummy = ListNode()
        p = dummy
        while q:
            curr = heapq.heappop(q)
            # print(curr)
            if curr:
                p.next = curr
                p = p.next
                if curr.next: heapq.heappush(q, curr.next)
                p.next = None
        return dummy.next

        

    #     k = len(lists)
    #     i = 0
    #     j = (k - 1) // 2
    #     tmp = []
    #     tmp2 = []
    #     while len(tmp2) != 1:
    #         # i = 0
    #         # j = (k - 1) // 2
    #         tmp = []
    #         while i <= j and i < (k - 1) // 2 and j < k:
    #             tmp.append(self.merge(lists[i], lists[j]))
    #             i += 1
    #             j += 1
    #         if i < (k - 1) // 2 - 1:
    #             tmp.append(lists[i + 1])
    #         if j < k - 1:
    #             tmp.append(lists[j + 1])
    #         tmp2 = tmp
    #     return tmp2[0]
    # def merge(self, l1, l2):
    #     p1 = l1
    #     p2 = l2
    #     dummy = ListNode()
    #     p = dummy
    #     while p1 and p2:
    #         if p1.val < p2.val:
    #             p.next = p1
    #             p = p.next
    #             p1 = p1.next
    #             p.next = None
    #         else:
    #             p.next = p2
    #             p = p.next
    #             p2 = p2.next
    #             p.next = None
    #     if p1:
    #         p.next = p1
    #     if p2:
    #         p.next = p2
    #     return dummy.next