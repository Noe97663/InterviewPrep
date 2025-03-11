# given a 2D list of numbers representing the board
# determine whether it is a valid board

## Brute force - bruh - O(n^2), O(1)
## Hash sets - use row, col, square sets - O(n^2), O(1)

#sets
from collections import defaultdict
def isValidSudoku(board: List[List[str]]) -> bool:
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)  

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if ( board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r // 3, c // 3)]):
                return False

            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    return True