class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        self.head = None

    def addAtHead(self, val):
        curr = ListNode(val)
        if self.head:
            curr.next = self.head
        self.head = curr

    def _getNodeAtIndex(self, index):
        if not self.head or index < 0:
            return None
        curr = self.head
        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1
        return curr

    def addAtTail(self, val):
        curr = ListNode(val)
        if not self.head:
            self.head = curr
        else:
            prev = self.head
            while prev.next is not None:
                prev = prev.next
            prev.next = curr

    def addAtIndex(self, index, val):
        new_node = ListNode(val)
        prev = self._getNodeAtIndex(index-1)
        curr = prev.next
        new_node.next = curr
        prev.next = new_node

    def deleteAtIndex(self, index):
        if index == 0:
            self.head = self.head.next
            return
        elif index < 0:
            return
        else:
            prev = self._getNodeAtIndex(index - 1)
            if not prev:
                return
            curr = prev.next
            prev.next = curr.next


if __name__ == "__main__":
    obj = MyLinkedList()
    obj.addAtHead(5)
    obj.addAtTail(7)
    obj.addAtHead(10)
    obj.addAtHead(32)
    obj.addAtIndex(2, 56)
    obj.deleteAtIndex(0)
    obj.deleteAtIndex(2)
    obj.deleteAtIndex(8)
    curr = obj.head
    while curr is not None:
        print(curr.val)
        print("\n")
        curr = curr.next