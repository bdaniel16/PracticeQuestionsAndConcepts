class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        s_ptr = head
        f_ptr = head.next
        while s_ptr != f_ptr:
            if f_ptr is None or f_ptr.next is None:
                return False
            s_ptr = s_ptr.next
            f_ptr = f_ptr.next.next
        return True

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        s_ptr = head
        f_ptr = head.next
        while s_ptr != f_ptr:
            if f_ptr is None or f_ptr.next is None:
                return None
            s_ptr = s_ptr.next
            f_ptr = f_ptr.next.next
        return s_ptr


if __name__ == "__main__":
    sol = Solution()
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    #print(sol.hasCycle(n1))
    print(sol.detectCycle(n1).val)