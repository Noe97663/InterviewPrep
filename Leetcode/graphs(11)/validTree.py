# given nodes and edges, determine if the graph is a tree
# all nodes must be connected, no cycles

## Brute force  - Build an adjacency matrix, DFS/BFS through the graph,
##                keeping track of visited nodes (and prev visited)
##                - O( V + E ), O( V + E )


def validTree(n: int, edges: [[int]]) -> bool:
    if len(edges) > (n - 1):
        return False

    # build adjacency matrix
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visit = set()

    def dfs(node, par):
        if node in visit:
            return False
        visit.add(node)
        for nei in adj[node]:
            # if a node is a parent/previously visited
            # an edge backwards does not mean its a cycle
            if nei == par:
                continue
            if not dfs(nei, node):
                return False
        return True

    # check cycles and all nodes visited
    return dfs(0, -1) and len(visit) == n
