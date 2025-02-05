# Invert the binary tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## DFS - stack or recursive - O(n), O(n)
## BFS - queue - O(n), O(n)


def invertTree(root: [TreeNode]) -> [TreeNode]:
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root
