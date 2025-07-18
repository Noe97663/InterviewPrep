# left to right, level order traversal


from buildTree import TreeNode


## DFS - stack or recursive - O(n), O(n)
## BFS - queue - O(n), O(n)

import collections


def maxDepth(root: [TreeNode]) -> int:
    def levelOrder(root: [TreeNode]) -> [[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res
