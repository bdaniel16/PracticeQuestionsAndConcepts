class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preOrderRec(root):
    if not root:
        return []
    return [root.val] + preOrderRec(root.left) + preOrderRec(root.right)


def preOrderIter(root):
    if not root:
        return []
    res = []
    stk = [root]
    while stk:
        item = stk.pop()
        res.append(item.val)
        if item.right is not None:
            stk.append(item.right)
        if item.left is not None:
            stk.append(item.left)
    return res


def inOrderRec(root):
    if not root:
        return []
    return inOrderRec(root.left) + [root.val] + inOrderRec(root.right)


def inOrderIter(root):
    if not root:
        return []
    res, stck = [], []
    curr = root
    while curr or stck:
        while curr is not None:
            stck.append(curr)
            curr = curr.left
        curr = stck.pop()
        res.append(curr.val)
        curr = curr.right
    return res


def postOrderRec(root):
    if not root:
        return []
    return postOrderRec(root.left) + postOrderRec(root.right) + [root.val]


def postOrderIter(root):
    if not root:
        return []
    res, stck = [], []
    curr = root
    while stck:
        while curr.left is not None:
            stck.append(curr)
            curr = curr.left
        while curr.right is not None:
            curr = curr.right
            stck.append(curr)
        res.append(stck.pop().val)


if __name__ == "__main__":
    c = TreeNode(1)
    b = TreeNode(2)
    a = TreeNode(4, left=c)
    root = TreeNode(3, left=b, right=a)

    # print(preOrderRec(root))
    # print(preOrderIter(root))

    #print(inOrderRec(root))
    #print(inOrderIter(root))

    #print(postOrderRec(root))
    print(postOrderIter(root))