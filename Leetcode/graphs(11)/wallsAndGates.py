# water = -1
# treasure = 0
# mountain = INF

## BFS from the treasure out - (m. n), O(m. n)

## made mistake of doing every cell to closest treasure
## more efficient to do all treasure to cells

def islandsAndTreasure(grid: [[int]]) -> None:
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    q = deque()

    def addCell(r, c):
        if (min(r, c) < 0 or r == ROWS or c == COLS or
            (r, c) in visit or grid[r][c] == -1
        ):
            return
        visit.add((r, c))
        q.append([r, c])

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                q.append([r, c])
                visit.add((r, c))

    dist = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            grid[r][c] = dist
            addCell(r + 1, c)
            addCell(r - 1, c)
            addCell(r, c + 1)
            addCell(r, c - 1)
        dist += 1