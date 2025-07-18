# Check if the given subtree exists in a tree


from buildTree import TreeNode

## Recursive DFS - at each node call sameTree function - O(n. m), O(m+n)


def isSubtree(root: [TreeNode], subRoot: [TreeNode]) -> bool:
    if not subRoot:
        return True
    if not root:
        return False

    if sameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def sameTree(root: [TreeNode], subRoot: [TreeNode]) -> bool:
    if not root and not subRoot:
        return True
    if root and subRoot and root.val == subRoot.val:
        return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)
    return False
