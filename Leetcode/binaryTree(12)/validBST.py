# Check if the BST is valid
from buildTree import TreeNode

## DFS - O(n), O(n)
## BFS - O(n), O(n)

import collections


# DFS
def isValidBST(root: [TreeNode]) -> bool:
    def valid(node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False

        return valid(node.left, left, node.val) and valid(node.right, node.val, right)

    return valid(root, float("-inf"), float("inf"))


# BFS
def isValidBST(root: [TreeNode]) -> bool:
    if not root:
        return True

    q = collections.deque([(root, float("-inf"), float("inf"))])

    while q:
        node, left, right = q.popleft()
        if not (left < node.val < right):
            return False
        if node.left:
            q.append((node.left, left, node.val))
        if node.right:
            q.append((node.right, node.val, right))

    return True
