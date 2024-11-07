class ListNode:
    def __init__(self, x:int, node:'ListNode'=None) -> None:
        self.val:int = x
        self.next:ListNode = node
    
    @classmethod
    def fromList(cls, lst:list[int]):
        head = ListNode(lst[0])
        node = head
        for i in range(1, len(lst)):
            node.next = ListNode(lst[i])
            node = node.next
        return head
    
    @classmethod
    def fromListNode(cls, node:'ListNode'):
        head = ListNode(node.val)
        ls = head
        node_ = node
        while node_.next:
            ls.next = ListNode(node_.val)
            ls = ls.next
            node_ = node_.next
        return head
    
    def print(self):
        node = self
        while node:
            print(node.val)
            node = node.next
