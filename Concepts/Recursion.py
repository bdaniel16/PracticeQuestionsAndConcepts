# *************************************
# Contains solutions for:
# simple string reverse
# recursion string reverse
# Swap alternate pairs of linked lists.
# get row of Pascal triangle ( where current row value is sum of prev row column values)
# get fibonacci number using memoization
# climbing stairs using memoization
# *************************************
from typing import List


def strRev(ind, strg):
    if not strg or ind >= len(strg):
        return
    strRev(ind + 1, strg)
    print(strg[ind])

# "hello" -> "oellh" -> "olleh"
# "banana" -> "aabanb" -> "anbaab" ->"ananab"


def strRevRecursion(i, j, s):
    if i == j or i > j:
        return
    temp = s[i] # python one-liner: s[start], s[end] = s[end], s[start]
    s[i] = s[j]
    s[j] = temp
    strRevRecursion(i+1, j-1, s)


# Swap alternate pairs of linked lists.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.fib_map = {}

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head

        first_node = head
        second_node = head.next

        # swap
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node

    def getPascalRow(self, rowIndex: int) -> List[int]:
        # f(i,j)=f(i−1,j−1)+f(i−1,j)
        # f(i,j)=1wherej=1orj=i
        res = []
        for j in range(rowIndex + 1):
            res.append(self.helper(rowIndex, j))
        return res

    def helper(self, i, j):
        if i == j or j == 0:
            return 1
        else:
            return self.helper(i - 1, j - 1) + self.helper(i - 1, j)

    def fibonacciMemoization(self, n):
        if self.fib_map.get(n):
            return self.fib_map.get(n)
        if n == 0:
            return 0
        elif n < 2:
            return 1
        else:
            res = self.fibonacciMemoization(n-1) + self.fibonacciMemoization(n-2)

        self.fib_map[n] = res
        return res

    def climbStairs(self,n):
        memo = {}
        self.cbstHelper(0,n,memo)

    def cbstHelper(self, i, n, memo):
        if i == n:
            return 1
        elif i > n:
            return 0
        elif memo.get(i) and memo.get(i) > 0:
            return memo.get(i)
        memo[i] = self.cbstHelper(i+1,n, memo) + self.cbstHelper(i+2,n, memo)
        return memo[i]


if __name__ == "__main__":
    #st_list = ["h", "e", "l", "l", "o"]
    #st_list = ["b", "a", "n", "a", "n", "a"]
    # strRev(0, str)
    #strRevRecursion(0, len(st_list)-1, st_list)
    #print(st_list)
    sol = Solution()
    #print(sol.getPascalRow(1))
    #print(sol.fibonacciMemoization(0))
    print(sol.climbStairs(3))