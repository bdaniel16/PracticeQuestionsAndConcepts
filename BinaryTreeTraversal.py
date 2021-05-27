import queue

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preOrderTraversal(root):
    """
    DS: stack, list to keep order of visited nodes
    algo: put the root node on stack
    while node in stack:
    pop node
    visit node
	if node has right child
	add to stack
    if node has left child
	add to stack
    """
    if not root:
        return None
    traversal = []
    stck = [root]
    while stck:
        node = stck.pop()
        traversal.append(node.val)
        if node.right is not None:
            stck.append(node.right)
        if node.left is not None:
            stck.append(node.left)
    return traversal


def inorderTraversal(root):
    """
    left - root -right
    DS: stck, list for traversal
    algo: traverse left subtree
          visit root
          go right
    """
    if not root:
        return None
    traversal = []
    stck = []
    curr = root
    while stck or curr:
        while curr is not None:
            stck.append(curr)
            curr = curr.left
        curr = stck.pop()
        traversal.append(curr.val)
        curr = curr.right # no need to check curr.right is None, since that will cause an infinite loop
    return traversal


def postOrderTraversal(root):
    if not root:
        return None
    traversal = []
    stck = []
    curr = root
    while stck or curr:
        while curr is not None:
            stck.append(curr)
            curr = curr.left
        curr = stck[-1]
        if curr.right is not None and curr.right.val not in traversal:
            curr = curr.right
        else:
            stck.pop()
            traversal.append(curr.val)
            curr = None
    return traversal


def postOrderTraveralUsingTwoStacks(root):
    if not root:
        return None
    stck1, stck2 = [root], []
    while stck1:
        curr = stck1.pop()
        if curr.left:
            stck1.append(curr.left)
        if curr.right:
            stck1.append(curr.right)
        stck2.append(curr.val)
    return stck2[::-1]


def postOrderTraversalUsingOneStack(root):
    """
    A lot of edge cases while popping stck
    and accessing node's children have to be considered
    """
    traversal = []
    stck = []
    curr = root
    while True:
        while curr:
            if curr.right:
                stck.append(curr.right)
            stck.append(curr)
            curr = curr.left
        if stck:
            curr = stck.pop()
        if curr and curr.right and stck and curr.right == stck[len(stck) - 1]:
            prev = curr
            curr = stck.pop()
            stck.append(prev)
        elif curr:
            traversal.append(curr.val)
            curr = None
        if len(stck) < 1:
            break
    return traversal


def levelOrderTraversal(root):
    if not root:
        return None
    traversal = []
    que = queue.Queue()


def generateVeryLargeInput(arr):
    root = rnode = lnode = None
    l = False
    i = 0
    while i < len(arr):
        if not root:
            root = TreeNode(arr[i], left=TreeNode(arr[i + 1]), right=TreeNode(arr[i + 2])) # 64
            lnode = root.left # 12
            rnode = root.right # 18
            l = True
            i += 3
        elif l:
            if lnode:
                lnode.left = TreeNode(arr[i]) #
                lnode.right = TreeNode(arr[i + 1]) #
                lnode = lnode.left
            else:
                lnode = None
            i += 2
            l = False
        else:
            if rnode:
                rnode.left = TreeNode(arr[i]) #
                rnode.right = TreeNode(arr[i + 1]) #
                rnode = rnode.right
            else:
                rnode = None
            i += 2
            l = True

    return root


if __name__ == "__main__":
    a = TreeNode('A')
    i = TreeNode('C')
    d = TreeNode('E')
    c = TreeNode('D', left=i, right=d)
    b = TreeNode('B', left=a, right=c)
    g = TreeNode('H')
    f = TreeNode('I', left=g)
    e = TreeNode('G', right=f)
    root1 = TreeNode('F', left=b, right=e)
    four = TreeNode('4')
    five = TreeNode('5')
    six = TreeNode('6')
    seven = TreeNode('7')
    three = TreeNode('3', left=six, right=seven)
    two = TreeNode('2', left=four, right=five)
    one = TreeNode('1', left=two, right=three)
    # print(preOrderTraversal(root))
    # print(inorderTraversal(root))
    # print(postOrderTraversal(root))
#     arr = [-64,12,18,-4,-53,None,76,None,-51,None,None,-93,3,None,-31,47,None,3,53,-81,33,4,None,-51,-44,
# -60,11,None,None,None,None,78,None,-35,-64,26,-81,-31,27,60,74,None,None,8,-38,47,12,-24,None,-59,
# -49,-11,-51,67,None,None,None,None,None,None,None,-67,None,-37,-19,10,-55,72,None,None,None,-70,17,
# -4,None,None,None,None,None,None,None,3,80,44,-88,-91,None,48,-90,-30,None,None,90,-34,37,None,None,
# 73,-38,-31,-85,-31,-96,None,None,-18,67,34,72,None,-17,-77,None,56,-65,-88,-53,None,None,None,-33,86,
# None,81,-42,None,None,98,-40,70,-26,24,None,None,None,None,92,72,-27,None,None,None,None,None,None,
# -67,None,None,None,None,None,None,None,-54,-66,-36,None,-72,None,None,43,None,None,None,-92,-1,-98,
# None,None,None,None,None,None,None,39,-84,None,None,None,None,None,None,None,None,None,None,None,
# None,None,-93,None,None,None,98]
#     root2 = generateVeryLargeInput(arr)
#     print(postOrderTraversal(root2))
    # print(postOrderTraveralUsingTwoStacks(one))
    print(postOrderTraversalUsingOneStack(root1))


