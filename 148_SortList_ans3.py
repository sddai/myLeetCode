# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
这段代码的功能是对一个链表进行排序，使用了自底向上的归并排序的方法。具体的解释如下：

- 定义一个类Solution，有一个方法sortList，接受一个链表的头节点head作为参数，返回排序后的链表的头节点。
- 在方法中，首先定义了一个辅助函数merge，用来合并两个有序的链表，返回合并后的链表的头节点。这个函数的实现是使用一个虚拟头节点dummyHead，和三个指针temp, temp1, temp2。temp指向合并后的链表的最后一个节点，temp1和temp2分别指向两个待合并的链表的当前节点。使用一个while循环，比较temp1和temp2的值，将较小的节点接在temp后面，并更新temp, temp1, temp2。当temp1或temp2为空时，表示其中一个链表已经遍历完毕，将另一个链表接在temp后面。最后返回dummyHead.next，表示合并后的链表的头节点。
- 在sortList方法中，首先判断如果head为空，直接返回head，表示空链表不需要排序。
- 然后使用一个while循环，遍历链表，计算出链表的长度length，并将node指向链表的头节点head。
- 接着定义一个虚拟头节点dummyHead，并将其next指向head。定义一个变量subLength，表示每次归并排序的子链表的长度。初始时subLength为1，表示每个节点都是一个有序的子链表。
- 使用一个while循环，根据subLength的大小进行归并排序。初始时prev和curr都指向dummyHead.next，表示已经排序好的部分和未排序的部分的分界点。
- 使用一个while循环，将未排序的部分分成两个子链表，分别用head1和head2表示它们的头节点。使用两个for循环，根据subLength的大小找到head1和head2，并将它们从原来的链表中断开。使用一个变量succ表示下一对待合并的子链表的头节点。
- 调用merge函数，将head1和head2合并成一个有序的子链表，并用merged表示它的头节点。将merged接在prev后面，并更新prev到merged的最后一个节点。将curr更新为succ，表示继续处理下一对待合并的子链表。
- 将subLength左移一位，表示下一轮归并排序的子链表长度加倍。
- 返回dummyHead.next，表示排序后的链表的头节点。
'''

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next
        
        # 前边是merge函数
        if not head:
            return head
        
        length = 0
        node = head
        while node:
            length += 1   # 遍历链表，计算出链表的长度length
            node = node.next
        
        dummyHead = ListNode(0, head)
        subLength = 1
        while subLength < length:
            prev, curr = dummyHead, dummyHead.next   
            #初始时prev和curr表示已经排序好的部分prev和未排序的部分curr的分界点。
            while curr:
                # 第二次进入循环的时候，curr是上一次的succ，也就是尚未合并的那些节点
                head1 = curr # 将未排序的部分分成两个子链表，分别用head1和head2表示它们的头节点
                for i in range(1, subLength): # 两个for循环之一，根据subLength的大小找到head1和head2，并将它们从原来的链表中断开。
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next  # 将未排序的部分分成两个子链表，分别用head1和head2表示它们的头节点
                curr.next = None
                curr = head2
                for i in range(1, subLength):# 两个for循环之一，根据subLength的大小找到head1和head2，并将它们从原来的链表中断开。
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break
                # 前边这段的作用是按照步长subLength划分了两个子序列，分别记作head1和head2
                succ = None
                if curr:
                    succ = curr.next   # succ表示下一对待合并的子链表的头节点
                    curr.next = None
                
                merged = merge(head1, head2)  # 调用merge函数，合并
                prev.next = merged   # 将merged接在prev后面
                while prev.next:
                    prev = prev.next  # 更新prev到merged的最后一个节点，这样下一次进入内层while curr循环时，prev指向已排序部分的末尾，便于将本轮merged部分与下一轮已排序的merged接起来
                curr = succ   # 将curr更新为succ，表示继续处理下一对待合并的子链表。
            subLength <<= 1  # 将subLength左移一位，表示下一轮归并排序的子链表长度加倍。
        
        return dummyHead.next