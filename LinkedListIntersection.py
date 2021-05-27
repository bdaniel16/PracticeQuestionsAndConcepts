# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        - find length of both lists and check tails are equal(ref)
        - if tails not equal return
        - else, if lengths of lists not equal, longer list pointer is adv by the diff of length
        - adv both list pointers till the intersection is reached
        :param headA: ListNode
        :param headB: listNode
        :return: intersection node :ListNode or None
        3-1-5-9-7-2-1
                |
            4-6
        """
        len_a, tail_a = self._getLengthAndTail(headA)
        len_b, tail_b = self._getLengthAndTail(headB)
        if tail_a != tail_b:
            return None
        if len_a >= len_b:
            shorter = headB
            longer = headA
        else:
            shorter = headA
            longer = headB
        diff = abs(len_b - len_a)
        while diff > 0:
            longer = longer.next
            diff -= 1
        while shorter != longer:
            shorter = shorter.next
            longer = longer.next
        return shorter

    def _getLengthAndTail(self, head: ListNode) -> (int, ListNode):
        if not head:
            return 0, None
        curr = head
        length = 1
        while curr.next is not None:
            curr = curr.next
            length += 1
        return length, curr


if __name__ == "__main__":
    """
    3-1-5-9-7-2-1
            |
        4-6
    """
    A1 = ListNode(1)
    A2 = ListNode(2, A1)
    A3 = ListNode(7, A2)
    A4 = ListNode(9, A3)
    A5 = ListNode(5, A4)
    A6 = ListNode(1, A5)
    A7 = ListNode(3, A6)

    B1 = ListNode(6,A3)
    B2 = ListNode(4, B1)

    sol = Solution()
    intersect_node = sol.getIntersectionNode(A7, B2)
    if intersect_node:
        print(intersect_node.val)
    else:
        print("No intersection")
