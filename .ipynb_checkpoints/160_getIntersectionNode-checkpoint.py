# 【拼接法】将两个链表拼接在一起，则两个p指针相等的位置就是交点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        while p1 != p2:
            # p1 = p1.next
            # p2 = p2.next
            if p1 == None:
                p1 = headB
            else:
                p1 = p1.next
            if p2 == None:
                p2 = headA
            else:
                p2 = p2.next
        return p1

'''
# 解法二：预先跳过一段距离（预先计算两条链表的长度）
def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    lenA, lenB = 0, 0
    # 计算两条链表的长度
    p1, p2 = headA, headB
    while p1:
        lenA += 1
        p1 = p1.next
    while p2:
        lenB += 1
        p2 = p2.next
    # 让 p1 和 p2 到达尾部的距离相同
    p1, p2 = headA, headB
    if lenA > lenB:
        for i in range(lenA - lenB):
            p1 = p1.next
    else:
        for i in range(lenB - lenA):
            p2 = p2.next
    # 看两个指针是否会相同，p1 == p2 时有两种情况：
    # 1、要么是两条链表不相交，他俩同时走到尾部空指针
    # 2、要么是两条链表相交，他俩走到两条链表的相交点
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1
'''