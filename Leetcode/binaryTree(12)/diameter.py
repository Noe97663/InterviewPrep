# calculate the diameter of a tree (Longest possible path of nodes)

from buildTree import TreeNode

## Brute force - calculate heights at each node - O(n), O(n)
## DFS - traverse the tree, check sum of max lengths down sides 
##     - O(n), O(h)

def diameterOfBinaryTree(root: [TreeNode]) -> int:
    res = 0

    def dfs(root):
        # so we are comparing to all other res
        nonlocal res

        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        res = max(res, left + right)

        return 1 + max(left, right)

    dfs(root)
    return res

#iterative
def diameterOfBinaryTree(root:[TreeNode]) -> int:
    stack = [root]
    mp = {None: (0, 0)}

    while stack:
        node = stack[-1]

        if node.left and node.left not in mp:
            stack.append(node.left)
        elif node.right and node.right not in mp:
            stack.append(node.right)
        else:
            node = stack.pop()

            leftHeight, leftDiameter = mp[node.left]
            rightHeight, rightDiameter = mp[node.right]

            mp[node] = (1 + max(leftHeight, rightHeight),
                        max(leftHeight + rightHeight, leftDiameter, rightDiameter))

    return mp[root][1]