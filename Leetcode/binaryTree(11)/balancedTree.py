# Check whether the tree is balanced in height (diff <= 1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## Brute force - traverse the tree, calculate heights at each node
##             - O(n^2), O(n)
## DFS - Traverse the tree while keeping track of height and property
##     - O(n), O(h)

def isBalanced(root: [TreeNode]) -> bool:
    def dfs(root):
        if not root:
            return [True, 0]

        left, right = dfs(root.left), dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]