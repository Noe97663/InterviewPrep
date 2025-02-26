# build a binary tree from its pre-order + in-order representation


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## DFS - use pre-order[0] to find root, find the root in the in-order,
##       now you know there are n in the left sub tree (left of root in
##       the in order tree), take the first n from the pre-order and recurse
##       on the left, and the right - O(n^2), O(n)
## improvement - use a hashmap instead of .index() to make it O(n) - O(n), O(n)


def buildTree(self, preorder: [int], inorder: [int]) -> [TreeNode]:
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
    root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
    return root
