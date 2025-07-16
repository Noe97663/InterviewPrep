# Check if the trees are the same

from buildTree import TreeNode

## DFS - stack or recursive - O(n), O(n)
## BFS - queue - O(n), O(n)


def isSameTree(p: [TreeNode], q: [TreeNode]) -> bool:
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False
