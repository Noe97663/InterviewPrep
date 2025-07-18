# Invert the binary tree


from buildTree import TreeNode


## DFS - stack or recursive - O(n), O(n)
## BFS - queue - O(n), O(n)


def invertTree(root: [TreeNode]) -> [TreeNode]:
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root
