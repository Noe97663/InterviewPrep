# given a 2d matrix, calculate how many steps to 
# fully rot the grid, or -1
# 0 representing an empty cell
# 1 representing a fresh fruit
# 2 representing a rotten fruit

## BFS - O(m. n), O(m. n)
## BFS w/ no queue - O ((m.n)^2), O(1)

import collections

# BFS with no queue, need to go through m.n cells x times
# x is limited by m.n
def orangesRotting(grid: [[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    fresh = 0
    time = 0

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh += 1

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while fresh > 0:
        flag = False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    for dr, dc in directions:
                        row, col = r + dr, c + dc
                        if (row in range(ROWS) and 
                            col in range(COLS) and 
                            grid[row][col] == 1):
                            grid[row][col] = 3  
                            fresh -= 1
                            flag = True

        if not flag:
            return -1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 3:
                    grid[r][c] = 2  

        time += 1

    return time

#BFS - max it can add to queue is m.n cells
def orangesRotting(grid: [[int]]) -> int:
    q = collections.deque()
    fresh = 0
    time = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append((r, c))

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while fresh > 0 and q:
        length = len(q)
        for i in range(length):
            r, c = q.popleft()

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row in range(len(grid))
                    and col in range(len(grid[0]))
                    and grid[row][col] == 1
                ):
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
        time += 1
    return time if fresh == 0 else -1