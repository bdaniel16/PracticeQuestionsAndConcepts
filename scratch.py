import os


def jumpingOnClouds(c):
    min_dist = 0
    s_ptr = 0
    while s_ptr + 2 < len(c) - 1:
        if s_ptr + 1 > len(c) - 1:
            min_dist += 1
            break
        elif c[s_ptr] == 0:
            if c[s_ptr + 1] == 0:
                min_dist += 1
        elif c[s_ptr] == 1:
            if c[s_ptr + 1] == 0:
                min_dist += 1
        s_ptr += 2
    return min_dist


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        nd = Node(data)
        if head is None:
            return nd
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
        curr.next = nd
        return head


if __name__ == '__main__':
    mylist = Solution()
    head = None
    for i in [2, 4, 3, 1]:
        head = mylist.insert(head, i)
    mylist.display(head)
    c = [0, 1, 0, 0, 0, 1, 0]
    result = jumpingOnClouds(c)
    print(result)