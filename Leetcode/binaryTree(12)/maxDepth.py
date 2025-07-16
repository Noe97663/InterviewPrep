# Find max depth of the tree
from buildTree import TreeNode


## DFS - stack or recursive - O(n), O(n)
## BFS - queue - O(n), O(n)


def maxDepth(root: [TreeNode]) -> int:
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))
