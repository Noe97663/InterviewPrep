# Check if the trees are the same


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## DFS - stack or recursive - O(n), O(n)
## BFS - queue - O(n), O(n)


def isSameTree(p: [TreeNode], q: [TreeNode]) -> bool:
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False
