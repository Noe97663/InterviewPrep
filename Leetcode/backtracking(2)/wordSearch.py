# word search in a grid

## cmon bruh - O(R. C. (4-1)^n), O(n)


def exist(board: [[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (
            r < 0
            or c < 0
            or r >= ROWS
            or c >= COLS
            or word[i] != board[r][c]
            or board[r][c] == "#"
        ):
            return False

        board[r][c] = "#"
        res = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )
        board[r][c] = word[i]
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True
    return False
