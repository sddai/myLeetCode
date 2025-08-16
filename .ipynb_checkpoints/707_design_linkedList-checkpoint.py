'''
# 报错的样例：
 1. 没判断index<0
 2. addAtIndex要判断是不是最后一个节点（更好的办法是加一个tail节点）
class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(val=0, next=None, prev=None)
        self.length = 0

    def get(self, index: int) -> int:
        p = self.head
        if index >= self.length:
            return None
        for i in range(index+1):
            p = p.next
        return p.val   # 这里不要返回p，而要返回p.val，否则会TypeError
        
    def addAtHead(self, val: int) -> None:
        p = self.head
        add_node = ListNode(val=val, next=p.next, prev=p)
        if p.next:
            p.next.prev = add_node
            p.next = add_node
        else:
            p.next = add_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        n = self.length
        p = self.head
        for i in range(n):
            p = p.next
        add_node = ListNode(val=val, next=None, prev=p)
        p.next = add_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:   # 这里要将index和插入位置对应起来
        p = self.head
        if index >= self.length:
            return None
        for i in range(index):
            p = p.next  # 此时p指向index前一个节点
        add_node = ListNode(val=val, next=p.next, prev=p)
        p.next.prev = add_node
        p.next = add_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        p = self.head
        if index >= self.length:
            return None
        for i in range(index+1):
            p = p.next
        if p.next:
            p.prev.next = p.next
            p.next.prev = p.prev
        else:
            p.prev.next = None
        self.length -= 1


["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get",      "addAtHead","addAtIndex","addAtHead"]
[[],            [7],        [2],         [1],        [3,0],       [2],            [6],        [4],        [4](报错),  [4],        [5,0],       [6]]

输出：
[null,          null,       null,        null,       null,        null,            null,      null,       null,       null,       null,        null]
预期结果：
[null,          null,       null,        null,       null,        null,            null,      null,       4,          null,       null,        null]

还是上述用例，在index的判断中加上index<0返回-1的操作，输出变成：（get(4) = -1, error）
输出：
[null,null,null,null,null,null,null,null,-1,null,null,null]
预期结果：
[null,null,null,null,null,null,null,null,4,null,null,null]

因此，说明错误出在index的判断上

在每个函数中增加print length之后，上述测试用例的stdout是：
addHead 1
addHead 2
addHead 3
deleteIndex 2
addHead 3
addTail 4
addHead 5
addHead 6

说明addAtIndex没起作用
'''
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# 正确的程序：
class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(val=0, next=None, prev=None)
        self.length = 0

    def get(self, index: int) -> int:
        p = self.head
        if index >= self.length or index < 0:
            return -1
        for i in range(index+1):
            p = p.next
        print("get", self.length)
        return p.val   # 这里不要返回p，而要返回p.val，否则会TypeError
        
    def addAtHead(self, val: int) -> None:
        p = self.head
        add_node = ListNode(val=val, next=p.next, prev=p)
        if p.next:
            p.next.prev = add_node
            p.next = add_node
        else:
            p.next = add_node
        self.length += 1
        print("addHead", self.length)

    def addAtTail(self, val: int) -> None:
        n = self.length
        p = self.head
        for i in range(n):
            p = p.next
        add_node = ListNode(val=val, next=None, prev=p)
        p.next = add_node
        self.length += 1
        print("addTail", self.length)

    def addAtIndex(self, index: int, val: int) -> None:   # 这里要将index和插入位置对应起来
        p = self.head
        if index > self.length or index < 0:
            return None
        for i in range(index):
            p = p.next  # 此时p指向index前一个节点
        add_node = ListNode(val=val, next=p.next, prev=p)
        if p.next: # 即，如果p不是最后一个节点
            p.next.prev = add_node
            p.next = add_node
        else:
            p.next = add_node
        self.length += 1
        print("addIndex", self.length)

    def deleteAtIndex(self, index: int) -> None:
        p = self.head
        if index >= self.length:
            return None
        for i in range(index+1):
            p = p.next
        if p.next:
            p.prev.next = p.next
            p.next.prev = p.prev
        else:
            p.prev.next = None
        self.length -= 1
        print("deleteIndex", self.length)



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)