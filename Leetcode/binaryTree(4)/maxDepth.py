# Find max depth of the tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## DFS - stack or recursive - O(n), O(n)
## BFS - queue - O(n), O(n)


def maxDepth(root: [TreeNode]) -> int:
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))
