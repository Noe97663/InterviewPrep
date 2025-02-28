# count the number of unconnected components in the undirected graph
# given number of nodes (n), edges

## DFS/BFS - build adjacency matrix, array of n False, mark visits during
##           traversal - O( V + E ), O( V + E )
## DSU shi - O( V + E ), O(V)


# Disjoint Set Union


# parent - [ array of parent pointers]
# rank - [ array of size of component ]
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True


class Solution:
    def countComponents(self, n: int, edges: [[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res


# DFS
def countComponents(n: int, edges: [[int]]) -> int:
    adj = [[] for _ in range(n)]
    visit = [False] * n
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(node):
        for nei in adj[node]:
            if not visit[nei]:
                visit[nei] = True
                dfs(nei)

    res = 0
    for node in range(n):
        if not visit[node]:
            visit[node] = True
            dfs(node)
            res += 1
    return res
