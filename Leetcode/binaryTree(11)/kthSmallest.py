# given a BST, find the k'th number


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## Brute force - traverse all nodes, put into array,
##               sort array - O(n logn), O(n)
## In-order Traversal - In-order traversal, put into array,
##                      return k'th element - O(n), O(n)
## DFS using in-order concept - slightly better - O(n), O(n)


# In-order traversal
def kthSmallest(root: [TreeNode], k: int) -> int:
    arr = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        arr.append(node.val)
        dfs(node.right)

    dfs(root)
    return arr[k - 1]


# Iterative DFS
def kthSmallest(self, root: [TreeNode], k: int) -> int:
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right
