# Find the (parent) node between p and q


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## Recursion - O(h), O(h)
## Iteration - Optimal - O(h), O(1)


# Iterative
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    cur = root
    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur


# Recursive (conditions are the same, just written differently)
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or not p or not q:
        return None
    if max(p.val, q.val) < root.val:
        return lowestCommonAncestor(root.left, p, q)
    elif min(p.val, q.val) > root.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root
