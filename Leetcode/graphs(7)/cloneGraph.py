# Given a list of fully connected nodes as an adjacency list
# Make a deep copy of the given graph


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


## DFS - DFS through list, use hashmap to keep track of nodes
##       already created, connect nodes to neighbors - O(V+E), O(V)
## BFS - same as above with BFS


def cloneGraph(node: [Node]) -> [Node]:
    oldToNew = {}

    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]

        copy = Node(node.val)
        oldToNew[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node) if node else None
