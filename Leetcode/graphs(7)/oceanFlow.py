# Given a graph of land heights determine from which cells
# water can flow to the two oceans, one on top and left
# other on bottom and right

## Backtracking - Use recursive backtracking for each cell of the
##                graph to see if you can reach both oceans
##              - O( m. n. 4^(m.n) ), O(m. n)
## DFS/BFS - Use DFS/BFS to find all cells reachable from each ocean,
##           find the intersection of both sets - O(m. n), O(m. n)

## the difference in the above methods is that
## backtracking starts from the cell and tries to reach both oceans
## dfs/bfs starts from the oceans and sees which cells are reachable


# DFS
def pacificAtlantic(heights: [[int]]) -> [[int]]:
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visit, prevHeight):
        # already reached / out of bounds / unreachable
        if (
            (r, c) in visit
            or r < 0
            or c < 0
            or r == ROWS
            or c == COLS
            or heights[r][c] < prevHeight
        ):
            return
        visit.add((r, c))
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])

    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS - 1, atl, heights[r][COLS - 1])

    res = []
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])
    return res


# backtracking
def pacificAtlantic(heights: [[int]]) -> [[int]]:
    ROWS, COLS = len(heights), len(heights[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    pacific = atlantic = False

    def dfs(r, c, prevVal):
        nonlocal pacific, atlantic
        if r < 0 or c < 0:
            pacific = True
            return
        if r >= ROWS or c >= COLS:
            atlantic = True
            return
        if heights[r][c] > prevVal:
            return

        tmp = heights[r][c]
        heights[r][c] = float("inf")
        for dx, dy in directions:
            dfs(r + dx, c + dy, tmp)
            if pacific and atlantic:
                break
        heights[r][c] = tmp

    res = []
    for r in range(ROWS):
        for c in range(COLS):
            pacific = False
            atlantic = False
            dfs(r, c, float("inf"))
            if pacific and atlantic:
                res.append([r, c])
    return res
