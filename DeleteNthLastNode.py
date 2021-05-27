# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    1-2-3-4-5
    n =2 --> 4
    """

    def findNthFromEnd(self, head: ListNode, n: int):
        if not head:
            return 0
        index = self.findNthFromEnd(head.next, n) + 1
        if index == n:
            print(head.val)
        return index

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        prev = dummy
        for _ in range(1, n+2):
            curr = curr.next
        while curr is not None:
            curr = curr.next
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next


if __name__ == "__main__":
    l5 = ListNode(5)
    l4 = ListNode(4, l5)
    l3 = ListNode(3, l4)
    #l2 = ListNode(2, l3)
    l2 = ListNode(2)
    l1 = ListNode(1, l2)

    sol = Solution()
    #sol.findNthFromEnd(l1, 0)
    head = sol.removeNthFromEnd(l1, 2)
    print(head.val)